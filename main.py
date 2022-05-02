# import all libraries
import pandas as pd
import unittest
import argparse
import pandas as pd
import path
import sys
import csv

# import all sub-functions from other .py files
from Features import inspect_stock, basic_stock_stat, stock_ROI, helper

# read all available data
nasdaq_df = pd.read_csv("Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")

def read_input():
    """
    Objective:
    This function checks the user input for the command line app and runs the valid corresponding feature.

    Input Signature:

    First Argument: specifies which feature will be used
    -inspect: calls the inspect stock feature
    -basic_stat: calls the basic stock stat feature
    -stock_ROI: calls the stock ROI feature

    proceeding arguments for -inspect:
    ticker: this is the ticker symbol for the stock, ex. AAPL
    year: this is the specified year of the stock that the user wants to find, ex. 2021
    month: this is the specified month of the stock that the user wants to find, ex. 3
    query: This is the type of statistic that the user wants, ex. Open

    Output:
    The statistic (specified by the query input argument) of a stock (specified by ticker symbol)
    at a certain point in time (specified by month and year of investment).

    """

    # calls a helper method for reading file so ensures there is only 1 level of abstraction
    fileName = "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv"
    nasdaq_df = helper.get_dataframe(fileName)
    # num_of_args = len(sys.argv)

    return run_feature_called()
    
    # python3 main.py -inspect_stock AMZN 2022 3 Volume
    # python3 main.py -basic_stat AMZN
    # python3 main.py -stock_ROI AMZN 2011 12 Low 2022 3 High

def run_feature_called():
    num_of_args = len(sys.argv)
    if num_of_args == 1:
        print("No feature Input! Try using the arguments -inspect, -basic_stat, or -stock_ROI")
        return False
    
    feature = str(sys.argv[1])
    if feature == "-inspect":
        return inspect_stock.find_query_input()

    elif feature == "-basic_stat":
        return basic_stock_stat.get_dates_input()

    elif feature == "-stock_ROI":
        ticker = str(sys.argv[2])
        date_invest = [int(sys.argv[3]), int(sys.argv[4])]
        date_divest = [int(sys.argv[6]), int(sys.argv[7])]
        buying_price = str(sys.argv[5])
        selling_price = str(sys.argv[8])
        return stock_ROI.main_stock_ROI(ticker, date_invest, date_divest, buying_price, selling_price, data_file = "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
            

    else:
        return "Invalid feature! Try using the arguments -inspect, -basic_stat, or -stock_ROI"
"""
def check_number_of_arguments(check):
    num_of_args = len(sys.argv)
    if (check == "inspect") and (num_of_args != 5):
        print("There needs to be 4 more arguments after -inspect; TickerSymbol, Year, Month, Query")
        return False
    elif (check == "basic_stat") and (num_of_args != 2):
        print("There needs to be 1 more argument after -basic_stat: TickerSymbol")
        return False
    elif (check == "stock_ROI") and (num_of_args != 8):
        print("There needs to be 7 more arguments after -inspect; TickerSymbol, First Year, First Month, First Query, Second Year, Second Month, Second Query")
        return False
    return True
"""

if __name__ == '__main__':
    print(read_input())