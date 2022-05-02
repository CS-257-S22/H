# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

import pandas as pd
import argparse

#from inspect_stock import check_query
from Features import inspect_stock

#------------------------------

def terminal_call_stock_ROI():
    """
    This functions trigger the terminal input interface for feature stock_ROI
    """

    # using argparse to get terminal input
    parser = argparse.ArgumentParser(description = "Demonstrating Argparse Library")

    # each line add AN argument to our terminal inout
    parser.add_argument("ticker", type = str, help = "ticker symbol of the stock of interest")
    parser.add_argument("date_invest_year", type = int, help = "the year that you hypothetically bought the stock")
    parser.add_argument("date_invest_month", type = int, help = "the month that you hypothetically bought the stock")
    parser.add_argument("buying_price", type = str, help = "the price that you hypothetically bought the stock at\
        , choose between 'Open', 'Close', 'High', 'Close', and 'Adjusted Close'")
    parser.add_argument("date_divest_year", type = int, help = "the year that you hypothetically sold the stock")
    parser.add_argument("date_divest_month", type = int, help = "the month that you hypothetically sold the stock")
    parser.add_argument("selling_price", type = str, help = "the price that you hypothetically bought the stock at\
        , choose between 'Open', 'Close', 'High', 'Close', and 'Adjusted Close'")

    # parse all arguments
    args = parser.parse_args()

    # storing the entered arguments internally within our code for ease of access
    ticker = args.ticker
    date_invest = [args.date_invest_year, args.date_invest_month]
    date_divest = [args.date_divest_year, args.date_divest_month]
    buying_price = args.buying_price
    selling_price = args.selling_price

    return main_stock_ROI(ticker, date_invest, date_divest, buying_price, selling_price)

#------------------------------

def main_stock_ROI(ticker, date_invest, date_divest, buying_price, selling_price, data_file = "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv"):
    """
    1. Consider this the main() function of the feature stock_ROI
    2. It will check the validity of the input by calling input_is_valid()
    3. Then it will calculate the ROI of the stock by calling the backbone method.

    
    """

    # read in the data
    nasdaq_df = pd.read_csv(data_file)
    
   # check if the input is valid
    validity = all_input_is_valid_stock_ROI(nasdaq_df, ticker, date_invest, date_divest, buying_price, selling_price)

    if validity == True:

        # find the ROI of the stock if all inputs are appropriate
        ROI = backbone_stock_ROI(nasdaq_df, ticker, date_invest, date_divest, buying_price, selling_price)

        return ROI

    else:
        return(validity) # return the error message


#------------------------------

def all_input_is_valid_stock_ROI(dataframe, ticker, date_invest, date_divest, buying_price, selling_price):
    """
    This function check if all inputed values are appropriate

    Input: A series of values which will be checked as well as the ticker symbol for which the specified data is represntative of and the datafram which is
    the location of the dataset said data is located within

    Output: A boolean representing whether the parameters specified are appropriate

    Note: Should we print out the error messages and return false instead of just returning the error message
    """

    # check ticker
    if not in_dateframe(ticker, "Ticker Symbol", dataframe):
        return "INPUT ERROR: Invalid ticker symbol. Please choose one that exists within our data instead."

    # check invest date
    if not in_dateframe(date_invest[0], "Year", dataframe):
        return "INPUT ERROR: Invalid year for investment date."
    else: # check month if year is valid
        if not in_dateframe(date_invest[1], "Month", dataframe.loc[dataframe["Year"] == date_invest[0]]):
            return "INPUT ERROR: Invalid investment date. The given month is not in our data."
    
    # check divest date
    if not in_dateframe(date_divest[0], "Year", dataframe):
        return "INPUT ERROR: Invalid year for divestment date."
    else: # check month if year is valid
        if not in_dateframe(date_divest[1], "Month", dataframe.loc[dataframe["Year"] == date_divest[0]]):
            return "INPUT ERROR: Invalid divestment date. The given month is not in our data."

    # check the queries in question
    if not check_query(buying_price):
        return "INPUT ERROR: Invalid buying price. Choose between 'Open', 'Close', 'High', 'Close', and 'Adjusted Close' only."
    if not check_query(selling_price):
        return "INPUT ERROR: Invalid selling price. Choose between 'Open', 'Close', 'High', 'Close', and 'Adjusted Close' only."

    # if no error is encountered, return True
    return True

#------------------------------

def in_dateframe(value, column, dataframe):
    """
    Check if a value is within a column of a dataframe
    
    Input: A value we are looking for, the column it is located in and the location of the dataset we are checking within

    Output: A boolean representing whether or not the specified datapoint is found within the specified dataset
    """

    if value in dataframe[column].values:
        return True

    else:
        return False

#------------------------------

def backbone_stock_ROI(dateframe, ticker, date_invest, date_divest, buying_price, selling_price):
    """
    Description
        This function automatically calculate the ROI of a stock given the investment and divestment time.

    Input Signature:
        1. ticker symbol (string)
        2. date of investment (list); [year of investment, month of investment]
        3. date of divestment (list); [year of divestment, month of divestment]
        4. buying price (string, "Open", "Close", "Adjusted Close", "Low", "High"); default = "Open"
        5. selling price (string, "Open", "Close", "Adjusted Close", "Low", "High"); default = "Close"

    Output Signature:
        1. The calculated return on investment in percentage (float data format), for the specified stock.
    """

    # finding the invested amount
    investmet = float(dateframe.loc[(dateframe["Ticker Symbol"] == ticker) &\
        (dateframe["Year"] == date_invest[0]) &\
        (dateframe["Month"] == date_invest[1])]\
        [buying_price])

    # finding the divested amount
    divestment = float(dateframe.loc[(dateframe["Ticker Symbol"] == ticker) &\
        (dateframe["Year"] == date_divest[0]) &\
        (dateframe["Month"] == date_divest[1])]\
        [selling_price])

    # calculating ROI
    stock_ROI = percentage_difference(initial=investmet, final=divestment)
    
    return stock_ROI

#------------------------------

def percentage_difference(initial, final):
    """
    This function finds the percentage difference between 2 numbers.

    Input: Two numbers

    Output: Calculated difference of the two numbers
    """

    difference = (final - initial) / initial

    # return the percentage value
    return (difference * 100)

#------------------------------

if __name__ == '__main__':

    # print out the value or error message
    print("\n\nThe return of investment (%) is:\n", terminal_call_stock_ROI(), "\n\n")