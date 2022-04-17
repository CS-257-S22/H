import sys
import csv
import pandas as pd
import datetime
from helper import check_ticker

def find_query():
    """
    This function is the main function for feature 1 of our command line interface, inspect stock. 
    This function takes in command line arguments, 4 specifically listed below:

    ticker: this is the ticker symbol for the stock, ex. AAPL
    year: this is the specified year of the stock that the user wants to find, ex. 2021
    month: this is the specified month of the stock that the user wants to find, ex. 3
    query: This is the type of the 

    """

    nasdaq_df = pd.read_csv("Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
    nasdaq_df["Date"] = pd.to_datetime(nasdaq_df["Date"])

    num_of_args = len(sys.argv)
    ticker = str(sys.argv[1])
    year = int(sys.argv[2])
    month = int(sys.argv[3])
    query = str(sys.argv[4])

    if not check_num_args(num_of_args):
        print("There needs to be 4 arguments; TickerSymbol, Year, Month, Query")
        return

    if not check_ticker(ticker):
        print("Ticker not found in dataset")
        return

    if not check_date(ticker, year, month):
        print("Invalid Date")
        return
        
    date = [year, month]
    output = inspect(ticker, date, query, nasdaq_df)
    # print(actual_ticker, actual_date, actual_query)
    print(output)
    return output

def check_num_args(num_of_args):
    """This method insures there is the proper number of command line arugments". Returns true if there are 5 command line arugments and false if there is not exactly 5."""
    if num_of_args != 5:
        return False
    return True
    

def check_date(ticker, year, month):
    """This method checks to make sure that the specified date (year and month) is located within the dataset for the specified ticker symbol. Returns true if it is found and false if it is not."""
    fileName = "Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv"
    f = open(fileName, 'r', encoding = "UTF-8")
    with f as rFile:
        spamreader = csv.reader(rFile, delimiter=',')
        next(spamreader)
        for row in spamreader:
            if row[10] == ticker and row[3] == str(year) and row[2] == str(month):
                f.close
                return True
    f.close
    return False
    
# def check_year(year):
#     if (2010 <= year <= 2022):
#         return True
#     return False

# def check_month(month):
#     if (1 <= month <= 12):
#         return True
#     return False
    
def check_query(query):
    """This method checks whether the parameter query is valid and contained in our dataset. Returns true if valid and false if invalid."""
    list = ["Low", "Open", "Volume", "High", "Close", "AdjustedClose"]
    if query in list:
        return True
    return False

def inspect(ticker, date, query_stat, dataframe):
    """
    Author:
        1. Miles
        2. Nguyen

    Objective:
        1. Return the requested inquery stat of a stock for a specific date

    Input Signature:
        1. ticker symbol (string)
        2. year of investment (int64)
        3. month of investment (int64)
        4. query_stat (string, "Open", "Close", "Adjusted Close", "Low", "High")

    Output Signature
        1. The relevant metric (query_stat) of a stock (ticker symbol) at a certain point in time (month and year of investment)
    """

    row_of_interst = dataframe.loc[(dataframe['Ticker Symbol'] == ticker) & (dataframe['Year'] == date[0]) & (dataframe['Month'] == date[1])]

    return row_of_interst.iloc[0][query_stat]

find_query()