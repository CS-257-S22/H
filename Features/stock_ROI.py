# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

import pandas as pd
import argparse

#from inspect_stock import check_query
sys.path.append('Features')
from inspect_stock import check_query

#------------------------------

def terminal_call_stock_ROI():
    """
    Description:
        This functions trigger the terminal input interface for feature stock_ROI

    Input Signature:
        1. Nothing. The sole purpose of this function is to facilitate the use within the terminal.
        2. Within the terminal, however, the user needs to manually input:
            - ticker symbol
            - investment year
            - investment month
            - buying price
            - divestment year
            - divestment month
            - selling price

    Output Signature:
        1. Call upon the main_stock_ROI method and return whatever the said method returns
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
    Description
        1. This is the main() function of this feature stock_ROI
        2. It will check the validity of the input by calling input_is_valid()
        3. Then it will calculate and return the ROI of the stock by calling the backbone_stock_ROI method

    Input Signature:
        1. ticker symbol (string)
        2. date_invest (two-element list in the format [year, month])
        3. date_divest (two-element list in the format [year, month])
        4. buying price (a string, choose between 'Open', 'Close', 'High', 'Close', and 'Adjusted Close')
        5. selling price (a string, choose between 'Open', 'Close', 'High', 'Close', and 'Adjusted Close')
        6. data_file: the path to our .csv file
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
    Description:
        1. This function check if all inputed values are appropriate

    Input:
        1. the Pandas dataframe object that is read from our .csv file
        2. the ticker symbol
        3. the date of investment (two-element list in the format [year, month])
        4. the date of divestment (two-element list in the format [year, month])
        5. the buying price of the stock (a string, choose between 'Open', 'Close', 'High', 'Close', and 'Adjusted Close')
        6. the selling price of the stock (a string, choose between 'Open', 'Close', 'High', 'Close', and 'Adjusted Close')

    Output:
        1. A boolean representing whether the parameters specified are appropriate
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
    Description:
        Check if a value is within a column of a dataframe
    
    Input:
        1. the value we want to check
        2. the column that we want to check within
    
    Output:
        1. A boolean representing whether or not the specified datapoint is found within the specified column
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
    Description:
        This function finds the percentage difference between 2 numbers.

    Input:
        1. Two numbers (kinda obvious)

    Output:
        2. Calculated difference of the two numbers in percentage
    """

    difference = (final - initial) / initial

    # return the percentage value
    return (difference * 100)

#------------------------------

if __name__ == '__main__':

    # print out the value or error message
    print("\n\nThe return of investment (%) is:\n", terminal_call_stock_ROI(), "\n\n")