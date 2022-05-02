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
    --inspect: calls the inspect stock feature
    --basic_stat: calls the basic stock stat feature
    --stock_ROI: calls the stock ROI feature

    proceeding arguments for --inspect:
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

    #checks which feature is called
    return check_feature_call()
    
    # python3 main.py inspect_stock AMZN 2022 3 Volume
    # python3 main.py basic_stat AMZN
    # python3 main.py stock_ROI.py AMZN 2011 12 Low 2022 3 High

# def get_dataframe(fileName):
#     """
#     Objective:
#     Helper function for reading the dataset to avoid multiple layers of abstraction

#     Input:
#     Takes in the directory location of a desired dataset

#     Output: 
#     Dataset ready for use in command line functions shaped by pandas

#     """
#     nasdaq_df = pd.read_csv(fileName)
#     nasdaq_df["Date"] = pd.to_datetime(nasdaq_df["Date"])
#     return nasdaq_df

def check_feature_call():
    check_number_of_arguments("any args")
    feature = str(sys.argv[1])

    if feature == "--inspect":
        check_number_of_arguments("inspect")
    elif feature == "--basic_stat":
        check_number_of_arguments("basic_stat")
    elif feature == "--stock_ROI":
        check_number_of_arguments("stock_ROI")
    else:
        return "Invalid feature! Try using the arguments --inspect, --basic_stat, or --stock_ROI"

def check_number_of_arguments(check):
    num_of_args = len(sys.argv)
    print(num_of_args)
    if (check == "inspect") and (num_of_args != 5):
        return "There needs to be 4 more arguments after --inspect; TickerSymbol, Year, Month, Query"
    elif (check == "basic_stat") and (num_of_args != 2):
        return "There needs to be 1 more argument after --basic_stat: TickerSymbol"
    elif (check == "stock_ROI") and (num_of_args != 8):
        return "There needs to be 7 more arguments after --inspect; TickerSymbol, First Year, First Month, First Query, Second Year, Second Month, Second Query"
    elif check == "any args" and (num_of_args == 1):
        return "No feature input! Please input a valid feature."
    else:
        return "broken"

if __name__ == '__main__':
    read_input()