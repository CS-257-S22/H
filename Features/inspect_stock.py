# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

import path
# current directory
directory = path.Path(__file__).abspath()
# setting path to the directory with the feature
sys.path.append(directory.parent.parent)

from fileinput import filename
import sys
import csv
import pandas as pd
import datetime

#from Features import helper
import sys
sys.path.append('./Features')
from helper import *

def find_query_input():
    """
    Description:
        THIS IS THE MAIN FUNCTION OF THIS FEATURE, INSPECT_STOCK
        Calling upon helper methods, it returns the requested statistic of a stock at a given time

    Input Signature:
        1. ticker: this is the ticker symbol for the stock, ex. AAPL
        2. year: this is the specified year of the stock that the user wants to find, ex. 2021
        3. month: this is the specified month of the stock that the user wants to find, ex. 3
        4. query: This is the type of statistic that the user wants, ex. Open

    Output:
        1. The statistic (specified by the query input argument) of a stock (specified by ticker symbol)
            at a certain point in time (specified by month and year of investment).
    """

    # calls a helper method for reading file so ensures there is only 1 level of abstraction
    # fileName = "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv"
    fileName = "./Data/Polished/randomized_day_market.csv"
    nasdaq_df = get_dataframe(fileName)
    nasdaq_df = rename_database_friendly(nasdaq_df)


    num_of_args = len(sys.argv)
    # assigns command line arguments to variables with correct types by casting
    if not check_num_args(num_of_args):
        return "There needs to be 4 arguments; TickerSymbol, Year, Month, Query"

    ticker = str(sys.argv[2])
    year = int(sys.argv[3])
    month = int(sys.argv[4])
    query = str(sys.argv[5])

    # calls find_query function to get the actual statistic and print and return the result
    output = find_query(num_of_args, ticker, year, month, query, nasdaq_df)
    # print(output)
    return output

def find_query(num_of_args, ticker, year, month, query, dataframe):
    """
    Description:
        This function runs helper functions to check for the correct user input, including the 
        number of parameters and if the ticker symbol and date are in the dataset.

    Input Signature:
        1. Num_of_args: The number of arguments of the command line
        2. year: this is the specified year of the stock that the user wants to find, ex. 2021
        3. month: this is the specified month of the stock that the user wants to find, ex. 3
        4. query: This is the type of statistic that the user wants, ex. Open
        5. fileName: path of dataset to read
        6. dataframe: the dataset returned from get_dataframe()

    Output:
        1. The statistic (specified by the query input argument) of a stock (specified by ticker symbol)
            at a certain point in time (specified by month and year of investment).

    """

    # checks if command line arguments are the correct number
    if not check_num_args(num_of_args):
        return "There needs to be 4 arguments; TickerSymbol, Year, Month, Query"

    # checks if ticker symbol is in the dataset and returns error statement if not found
    if not check_ticker(ticker):
        return "Ticker not found in dataset"

    # checks if the inputted date is in dataset and returns error statement if not found
    if not check_date(ticker, year, month):
        print(ticker)
        print(year)
        print(month)
        return "Invalid Date"

    # checks if the inputted query is offered
    if not check_query(query):
        return "Invalid Query"
        
    # structures year and month into a list
    date = [year, month]

    # calls inspect function which finds the statistic and returns statistic
    output = inspect(ticker, date, query, dataframe)
    return output

def check_num_args(num_of_args):
    """
    Description:
        This helper method insures there is the proper number of command line arugments

    Input:
        1. Interger representing the number of arguments passed into the command line

    Output:
        1. Boolean representing whether or not there is the proper amount of command line arguments passed in
    """
    if num_of_args != 6:
        return False
    return True
    

def check_date(ticker, year, month): #might need to take in fileName if reading a csv
    """
    Description:
        This helper method checks to make sure that the specified date (year and month) is located within the dataset 
        for the specified ticker symbol.

    Input:
        1. The ticker that we wish to check whether its date is in our data
        2. Year which is the year we are looking for
        3. month which is the month we are looking for
        4. fileName which is the location of the dataset

    Output:
        1. A boolean representing whether or not the particular data point is located within the requested dataset
    """
    
    # f = open(fileName, 'r', encoding = "UTF-8")
    # with f as rFile:
    #     spamreader = csv.reader(rFile, delimiter=',')
    #     next(spamreader)
    #     for row in spamreader:
    #         if row[9] == ticker and row[3] == str(year) and row[2] == str(month):
    #             f.close
    #             return True
    # f.close
    cursor = teamh.database.cursor()
    cursor.execute("SELECT ticker, rec_year, rec_month FROM nasdaq")
    table = cursor.fetchall()

    for row in table:
        if row[0] == str(ticker) and row[1] == str(year) and row[2] == str(month):
            return True
    return False

def check_query(query):
    """
    Description:
        This helper method checks whether the parameter query is valid and contained in our dataset.
        Returns true if valid and false if invalid.

    Input:
        1. A string representing a requested query category from the dataset

    Output:
        1. Boolean representing whether or not the input query is a valid request
    """
    list = ["Low", "Open", "Volume", "High", "Close"]
    if query in list:
        return True

    return False

def inspect(ticker, date, query_stat, dataframe):
    """
    Objective:
        1. Return the requested query statistic of a stock for a specific date from the 
        dataset

    Input Signature:
        1. ticker symbol of stock (string)
        2. year of investment (int64)
        3. month of investment (int64)
        4. query_stat (string, "Low", "Open", "Volume" "High", "Close")

    Output Signature
        1. The relevant metric (query_stat) of a stock (ticker symbol) at a certain point in time (month and year of investment)
    """

    # locate the row that has the correct ticker and date value within our data
    row_of_interst = dataframe.loc[(dataframe['Ticker Symbol'] == ticker) & (dataframe['Year'] == date[0]) & (dataframe['Month'] == date[1])]

    # return the value at the column that is the requested query stat
    return row_of_interst.iloc[0][query_stat]

# main function to run find_query_input()
if __name__ == '__main__':
    print(find_query_input())