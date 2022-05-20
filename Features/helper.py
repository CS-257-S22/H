# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

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
    
    # f = open(fileName, 'r', encoding = "UTF-8")
    # with f as rFile:
    #     spamreader = csv.reader(rFile, delimiter=',')
    #     next(spamreader)
    #     for row in spamreader:
    #         if row[9] == ticker:
    #             f.close
    #             return True
    # f.close
    # return false

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

# def getExtremeDates(ticker):
#     if not check_ticker(ticker):
#         return "Please input a valid ticker symbol"

#     f = open("./Data/Polished/randomized_day_market.csv", 'r', encoding = "UTF-8")
#     firstDate = ""
#     lastDate = ""
#     with f as rFile:
#         spamreader = csv.reader(rFile, delimiter=',')
#         next(spamreader)
#         for row in spamreader:
#             if row[9] == ticker:
#                 firstDate = row[0]
#                 break
#         for row in spamreader:
#             if row[9] != ticker:
#                 lastDate = row[0]
#                 break
#     f.close

#     cursor.execute("SELECT ticker, rec_date FROM nasdaq")
#     table = cursor.fetchall()
#     for row in table:
#         if row[0] == ticker:
#             firstDate = row[1]
#             break
#     for row in table:
#         if row[9]

#     return firstDate, lastDate

def getMax(ticker):
    """
    Objective: Searches through a dataset (Only data on TSLA is recorded at this time so it is hardcoded) and returns
    the maximum recorded 'High' price for a particular stock (Only TSLA is acceptable at this time). Also returns the
    data of the highest recorded stock price.
    Input: Takes in a ticker symbol which must be recorded in our dataset (Only TSLA is acceptable at this time)
    Output: The maximum recorded value of particular stock and the date it was recorded on
    """
    if not check_ticker(ticker):
        return "Please input a valid ticker symbol"
    stat = float(0)
    maxDate = ""
    
    cursor.execute("SELECT ticker, high, rec_date FROM nasdaq")
    table = cursor.fetchall()

    for row in table:
        if row[0] == ticker:
            if (float(row[1]) > stat):
                stat = float(row[1])
                maxDate = row[2]
                
    return stat, maxDate
    
    # f = open("./Data/Polished/randomized_day_market.csv", 'r', encoding = "UTF-8")
    # with f as rFile:
    #     reader = csv.reader(rFile, delimiter=",")
    #     next(reader)
    #     for item in reader:
    #         if item[9] == ticker:
    #             if (float(item[7]) > stat):
    #                 stat = float(item[7])
    #                 maxDate = item[0]
    # f.close
    # return stat, maxDate

def getMin(ticker):
    """
    Objective: Searches through a dataset (Only data on TSLA is recorded at this time so it is hardcoded) and returns
    the maximum recorded 'High' price for a particular stock (Only TSLA is acceptable at this time). Also returns the
    data of the highest recorded stock price.
    Input: Takes in a ticker symbol which must be recorded in our dataset (Only TSLA is acceptable at this time)
    Output: The maximum recorded value of particular stock and the date it was recorded on
    """
    if not check_ticker(ticker):
        return "Please input a valid ticker symbol"
    stat = float(99999999999999999)
    minDate = ""

    cursor.execute("SELECT ticker, low, rec_date FROM nasdaq")
    table = cursor.fetchall()

    for row in table:
        if row[0] == ticker:
            if (float(row[1]) < stat):
                stat = float(row[1])
                minDate = row[2]
    
    return stat, minDate
    
    
    # f = open("./Data/Polished/randomized_day_market.csv", 'r', encoding = "UTF-8")
    # with f as rFile:
    #     reader = csv.reader(rFile, delimiter=",")
    #     next(reader)
    #     for item in reader:
    #         if item[9] == ticker:
    #             if (float(item[4]) < stat):
    #                 stat = float(item[4])
    #                 minDate = item[0]
    # f.close
    # return stat, minDate

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
    stock_df = pd.read_sql_query("select * from nasdaq;", teamh.database)
    stock_df = rename_database_friendly(stock_df)

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