import sys
import csv
import pandas as pd
# from inspect_stock import check_ticker

def get_dates():

    nasdaq_df = pd.read_csv("Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
    nasdaq_df["Date"] = pd.to_datetime(nasdaq_df["Date"])

    ticker = str(sys.argv[2])
    if not check_ticker(ticker):
        print("Ticker not found in dataset")
        return
   
    output = basic_stock_stat(ticker, nasdaq_df)
    print(output)
    return output

    
def check_ticker(ticker):
    fileName = "Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv"
    f = open(fileName, 'r', encoding = "UTF-8")
    with f as rFile:
        spamreader = csv.reader(rFile, delimiter=',')
        next(spamreader)
        for row in spamreader:
            if row[10] == ticker:
                f.close
                return True
    f.close
    return False 

        


# def basic_stock_stat_input():
#     """
#     Author:
#         1. Geoffrey
#         2. Jack

#     Objective:
#         1. Obtain user input from terminal

#     Input Signature:
#         1. None (pop-up prompt for user instead)

#     Output Signature:
#         1. ticker (string) 
#     """


#     return ticker # dataformat: string

# ----------------------------

def basic_stock_stat(ticker, dataframe):
    """
    Author: Nguyen Tran

    Objective:
        1. Find the earliest and latest record dates of a stock.

    Input Signature:
        1. ticker symbol (string)

    Output Signature:
        1. list [earliest year in record, earliest month in record]
        2. list [latest year in record, latest month in record]
    """

    # find the earliest dates
    earliest_date = find_earliest_or_latest_record(ticker, method = "earliest", dataframe = dataframe)

    # find the latest dates
    latest_date = find_earliest_or_latest_record(ticker, method = "latest", dataframe = dataframe)

    return earliest_date, latest_date

# ----------------------------

def find_earliest_or_latest_record(ticker, method, dataframe):


    if method == "earliest":

        # find the earliest year
        earliest_year = dataframe.loc[dataframe["Ticker Symbol"] == ticker]\
            ["Year"].min()

        # find the earliest month
        earliest_month = dataframe.loc[(dataframe["Ticker Symbol"] == ticker) &\
            (dataframe["Year"] == earliest_year)]\
            ["Month"].min()

        return [earliest_year, earliest_month]


    elif method == "latest":

        # find the latest year
        latest_year = dataframe.loc[dataframe["Ticker Symbol"] == ticker]\
            ["Year"].max()

        # find the latest month
        latest_month = dataframe.loc[(dataframe["Ticker Symbol"] == ticker) &\
            (dataframe["Year"] == latest_year)]\
            ["Month"].max()

        return [latest_year, latest_month]


get_dates()