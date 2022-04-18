import sys
import csv
import pandas as pd
from helper import check_ticker

def get_dates():
    """
    Objective:
        1. To read through our data file and find the earliest and latest 
        recorded dates of a particular stock by calling basic_stock_stat 
        helper method. 

    Input Signature:
        1. Takes in the ticker symbol through the command line

    Output Signature:
        1. Returns the earliest recorded date and latest
        recorded date of a stock

    """
    nasdaq_df = pd.read_csv("Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
    nasdaq_df["Date"] = pd.to_datetime(nasdaq_df["Date"])

    ticker = str(sys.argv[1])
    if not check_ticker(ticker):
        print("Ticker not found in dataset")
        return
   
    output = basic_stock_stats(ticker, nasdaq_df)
    print(output)
    return output

def basic_stock_stats(ticker, dataframe):
    """
    Objective:
        1. Find the earliest and latest record dates of a stock.

    Input Signature:
        1. ticker symbol (string)

    Output Signature:
        1. list [earliest year in record, earliest month in record]
        2. list [latest year in record, latest month in record]
    """

    # find the earliest year
    earliest_year = dataframe.loc[dataframe["Ticker Symbol"] == ticker]\
        ["Year"].min()

    # find the earliest month
    earliest_month = dataframe.loc[(dataframe["Ticker Symbol"] == ticker) &\
        (dataframe["Year"] == earliest_year)]\
        ["Month"].min() 


    # find the latest year
    latest_year = dataframe.loc[dataframe["Ticker Symbol"] == ticker]\
        ["Year"].max()

    # find the latest month
    latest_month = dataframe.loc[(dataframe["Ticker Symbol"] == ticker) &\
        (dataframe["Year"] == latest_year)]\
        ["Month"].max()

    # filtering the main dataframe to contains only rows of the stock in question
    ticker_dataframe = dataframe.loc[dataframe["Ticker Symbol"] == ticker]

    # find the earliest and latest year in the dataframe

    return [earliest_year, earliest_month], [latest_year, latest_month]


def find_extreme_time(time, dataframe):

    """
    Input Signature:
        1. time (str, "Year" or "Month")
        2. dataframe(a filtered Pandas dataframe)

    Output Signature:
        1. min extreme time (int64)
        2. max extreme time (int64)
    """

    return dataframe[time].min(), dataframe[time].max()

get_dates()

#     # find the earliest dates
#     earliest_date = find_earliest_or_latest_record(ticker, method = "earliest", dataframe = dataframe)

#     # find the latest dates
#     latest_date = find_earliest_or_latest_record(ticker, method = "latest", dataframe = dataframe)

#     return earliest_date, latest_date

# # ----------------------------

# def find_earliest_and_latest_record(ticker, dataframe):

    