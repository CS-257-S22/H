# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

from basic_stock_stat import *

import pandas as pd
import path
# current directory
directory = path.Path(__file__).abspath()
# setting path to the directory with the feature
sys.path.append(directory.parent.parent)

# database import
import psycopg2
import psqlConfig as config

import csv

# a class to read from the psql database
class DataSource():
        
    #------------------------------

    def __init__(self):
        """
        Establish the first instance by connecting to the database
        """

        self.database = self.connect()

    #------------------------------

    def connect(self):
        """
        Connect to the team's database using the given credentials on perlman
        """


        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host = "localhost")
        
        except Exception as e:
            print("Connection error: ", e)
            exit()

        return connection

# creating a copy of the team's database
teamh = DataSource()
cursor = teamh.database.cursor()

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

def get_dataframe():

    """
    Description:
        1. Helper function for reading the dataset to avoid multiple layers of abstraction

    Input:
        1. Path to the file of our dataset

    Output: 
        2. Dataset ready for use in command line functions shaped by pandas
    """

    # read the database from psql server to pandas and rename the columns
    nasdaq_df = pd.read_sql_query("select * from nasdaq;", teamh.database)
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
    earliest_date, latest_date = stock_extreme_dates(ticker, dataframe)

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