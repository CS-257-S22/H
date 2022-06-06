# setting path to the directory with the features
import sys
sys.path.append(sys.path[0]+'/./Features')

# UNIVERSAL IMPORT
from universal_import import *

# import other features
import basic_stock_stat
import inspect_stock
import stock_ROI

def check_basicTicker(ticker):
    """
    Description:
        Runs our check_ticker method with preset dataset instead of taking one as a parameter

    Input:
        1. Ticker symbol of the company you are looking for

    Output:
        1. Returns the result of check_ticker(ticker, fileName) where fileName is preset to a default file
    """
    return check_ticker(ticker)

def check_ticker(ticker): #needs to take in filename if using csv
    """
    Description:
        1. Ensure that the ticker parameter is located within our dataset and is thus a valid ticker symbol

    Input:
        1. The requested ticker symbol that we are trying to identify whether or not it is in the dataset
        2. fileName which is the location of our dataset

    Output:
        1. A boolean representing whether or not the requested ticker symbol is found within the reference dataset   
    """

    cursor.execute("SELECT ticker FROM nasdaq")
    table = cursor.fetchall()

    for row in table:
        if row[0] == str(ticker):
            return True
    return False

def get_max(inputTicker):
    """
    Description: 
        1. Helper function which locates the highest recorded stock price in the data set of a particular stockand returns the value and date it was recorded on. 
    Input: 
        1. Takes in a ticker symbol which must be recorded in our dataset (Only TSLA is acceptable at this time)
    Output: 
        1. The maximum recorded value of particular stock and the date it was recorded on
    """
    if not check_ticker(inputTicker):
        return "Please input a valid ticker symbol"

    cursor.execute("SELECT rec_date, high FROM nasdaq WHERE ticker=%s ORDER BY high DESC;", (inputTicker, ))
    table = cursor.fetchall()
    return table[0][1], table[0][0]

    # cursor.execute("SELECT MAX(high) FROM nasdaq WHERE ticker = %s", (inputTicker, ))
    # maxVal = cursor.fetchall()[0]
    # cursor.execute("SELECT high, rec_date FROM nasdaq WHERE ticker = %s AND high = %s;", (inputTicker, maxVal))
    # table = cursor.fetchall()
    # return table


    # cursor.execute("SELECT high, rec_date FROM nasdaq WHERE ticker = %s AND high = (SELECT MAX(high) FROM nasdaq WHERE ticker = %s);", (inputTicker, ))
    # table = cursor.fetchall()
    # return table[0][0], table[0][1]

def get_min(inputTicker):
    """
    Description: 
        1. Helper function which locates the lowest recorded stock price in the data set of a particular stock and returns the value and date it was recorded on. 
    Input: 
        1. Takes in a ticker symbol which must be recorded in our dataset
    Output: 
        1. The minimum recorded value of particular stock and the date it was recorded on
    """
    if not check_ticker(inputTicker):
        return "Please input a valid ticker symbol"

    # get the dataframe from SQL server
    nasdaq_df = get_dataframe()

    # filter out only the ticker in question
    ticker_df = nasdaq_df[nasdaq_df["Ticker Symbol"] == inputTicker]

    # get the row with the minimum value of said ticker
    row_min = ticker_df[['Low']].idxmax()

    # get the minimum value and the date it occured of said ticker
    min_value = str(nasdaq_df.iloc[row_min]["Low"])[3:-5]
    min_value_date = str(nasdaq_df.iloc[row_min]["Date"])[3:-5]

    return min_value, min_value_date
        
    # cursor.execute("SELECT rec_date, low FROM nasdaq WHERE ticker=%s ORDER BY low;", (inputTicker, ))
    # table = cursor.fetchall()
    # return table[0][1], table[0][0]

    # cursor.execute("SELECT MIN(low) FROM nasdaq WHERE ticker = %s", (inputTicker, ))
    # minVal = cursor.fetchall()[0]
    # cursor.execute("SELECT low, rec_date FROM nasdaq WHERE ticker = %s AND low = %s;", (inputTicker, minVal))
    # table = cursor.fetchall()
    # return table

    # cursor.execute("SELECT rec_date, low FROM nasdaq WHERE ticker = %s AND low = (SELECT MIN(low) FROM nasdaq WHERE ticker = %s);", (inputTicker, ))
    # table = cursor.fetchall()
    # return table[0][0], table[0][1]

def get_dataframe():

    """
    Description:
        1. Helper function for reading the dataset to avoid multiple layers of abstraction

    Input:
        1. Path to the file of our dataset

    Output: 
        2. Dataset ready for use in command line functions shaped by pandas
    """

    # read the database from psql server to pandas
    nasdaq_df = pd.read_sql_query("select * from nasdaq;", teamh.database)

    # convert columns' type
    nasdaq_df["rec_year"].astype(int)
    nasdaq_df["rec_month"].astype(int)
    nasdaq_df["rec_day"].astype(int)

    # rename the columns
    nasdaq_df = rename_database_friendly(nasdaq_df)

    return nasdaq_df

def all_tickers():

    """
    DESCRIPTION:
        Find all ticker symbols (without duplicates) in any dataset

    INPUT SIGNATURE:
        1. filePath (string): the path to our dataframe

    OUTPUT SIGNATURE
        1. all_tickers_not_duplicate (list): a Python list contains all tickers (unordered)
    """

    # read the data from psql server and rename the columns
    stock_df = get_dataframe()

    # a list to store all tickers
    all_tickers = []

    # loop through the dataframe and get all tickers
    for i in range(len(stock_df)) :
        ticker = stock_df.loc[i, "Ticker Symbol"]
        all_tickers.append(ticker)

    # remove duplicate items
    all_tickers_not_duplicate = []
    
    for item in all_tickers:

        if item in all_tickers_not_duplicate:
            pass

        else:
            all_tickers_not_duplicate.append(item)

    return all_tickers_not_duplicate

def rename_database_friendly(dataframe):
    """
    DESCRIPTION:
        Due to technical issue, columns name have been changed when creating our team database.
        This method aim to rename all columns to the original ones in the .csv file (in pandas only).

    INPUT SIGNATURE:
        1. dataframe (Pandas dataframe): the Pandas dataframe read from the sql server

    OUTPUT SIGNATURE:
        1. dataframe (Pandas dataframe): the renamed dataframe
    """

    dataframe.rename(columns = {'rec_date':'Date', 'rec_day':'Day','rec_month':'Month', 'rec_year':'Year',\
        'low':'Low', 'rec_open':'Open', 'volume':'Volume', 'high':'High', 'rec_close':'Close',\
        'ticker':'Ticker Symbol'}, inplace = True)

    return dataframe

#------------------------------

def closest_available_record(ticker, date, dataframe):
    """
    DESCRIPTION:
        Input in a date, and this function will find out whether that date is available in the record for said ticker.
        If it doesn't, this function will return the closest date available.

    INPUT SIGNATURE:
        1. ticker (string)
        2. date (list): [year, month]
        3. dataframe: pandas

    OUTPUT SIGNATURE:
        1. True if the input date is in record
        2. the closest date if the input date is NOT in record
    """

    # find the earliest and latest dates
    earliest_date, latest_date = basic_stock_stat.stock_extreme_dates(ticker, dataframe)

    # convert everything to seconds for convenience
    earliest_seconds = to_seconds(earliest_date)
    latest_seconds = to_seconds(latest_date)
    date_seconds = to_seconds(date)

    if (earliest_seconds <= date_seconds) and (date_seconds <= latest_seconds):
        return True

    elif date_seconds > latest_seconds:
        return latest_date

    elif date_seconds < earliest_seconds:
        return earliest_date

#------------------------------

def to_seconds(date):
    """
    DESCRIPTION:
        Convert a list [year, month] to seconds for easy comparision
    """

    seconds = date[0] * 31557600 + date[1] * 2629800

    return seconds