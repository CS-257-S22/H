import sys
import csv
import pandas as pd
from helper import check_ticker

def get_dates_input():
    ticker = str(sys.argv[1])
    fileName = "Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv"
    get_dates(ticker, fileName)


def get_dates(ticker, fileName):
    """
    Objective:
        1. To read through our data file and find the earliest and latest 
        recorded dates of a particular stock by calling basic_stock_stat 
        helper method. 

    Input Signature:
        1. Takes in the ticker symbol and fileName

    Output Signature:
        1. Returns the earliest recorded date and latest
        recorded date of a stock

    """
    nasdaq_df = pd.read_csv(fileName)
    nasdaq_df["Date"] = pd.to_datetime(nasdaq_df["Date"])

    if not check_ticker(ticker, fileName):
        print("Ticker not found in dataset")
        return
   
    output = stock_extreme_dates(ticker, nasdaq_df)
    print(output)
    return output

def stock_extreme_dates(ticker, dataframe):
    """
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


if __name__ == '__main__':
    get_dates_input()

#     # find the earliest dates
#     earliest_date = find_earliest_or_latest_record(ticker, method = "earliest", dataframe = dataframe)

#     # find the latest dates
#     latest_date = find_earliest_or_latest_record(ticker, method = "latest", dataframe = dataframe)

#     return earliest_date, latest_date

# # ----------------------------

# def find_earliest_and_latest_record(ticker, dataframe):

    