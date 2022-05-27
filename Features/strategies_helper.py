# setting path to the directory with the features
import sys
sys.path.append(sys.path[0]+'/./Features')

# UNIVERSAL IMPORT
from universal_import import *

# import other features
import basic_stock_stat
import inspect_stock
import stock_ROI
import helper

#------------------------------

def calculate_market_values(date, dataframe):
    """
    DESCRIPTION:
        For a given month, calculate all the companies' market value and return them in descending order

    INPUT SIGNATURE:
        1. date (list): [year, month]
        2. dataframe (Pandas dataframe): the source of our data, usually nasdaq_df

    OUTPUT SIGNATURE:
        1. market_value_df (Pandas dataframe): 2 columns Ticker and Market Value, sorted by Market Value descendingly
    """

    # work on a safe copy of the data
    copy_df = dataframe.copy()

    # filter out the only month of interest
    conditioning_year = copy_df[(copy_df["Year"] != date[0])].index # is basically all the indices that needs to be dropped
    copy_df.drop(conditioning_year, inplace = True)
    conditioning_month = copy_df[(copy_df["Month"] != date[1])].index # is basically all the indices that needs to be dropped
    copy_df.drop(conditioning_month, inplace = True)

    # filter out companies that we don't have information on volume of shares
    with_volume_df = copy_df.loc[dataframe["Volume"] > 0]

    # empty list to store tickers
    ticker_symbols = []

    # empty list to store corresponding market value of the tickers
    market_values = []

    # NOTE: from the 2 lists above, we will create a Pandas dataframe with 2 columns, and sort descending by the market value column

    # loop through the filtered dataframe and calculate each company's market value
    for row in with_volume_df.index:

        ticker = with_volume_df["Ticker Symbol"][row]
        volume = with_volume_df["Volume"][row]
        close = with_volume_df["Close"][row] # we consider the closing price when finding out market cap

        market_value = close * volume

        # record the data
        ticker_symbols.append(ticker)
        market_values.append(market_value)

    # create a Pandas dataframe from the 2 lists to sort them
    data = {"Ticker" : ticker_symbols, "Market Value" : market_values}
    market_values_df = pd.DataFrame(data)

    # sort the dataframe
    market_values_df.sort_values(by = ["Market Value"], inplace = True, ascending = False)
    market_values_df.reset_index(inplace = True)

    return market_values_df

#------------------------------

def theXXX(number, date, dataframe):
    """
    DESCRIPTION:
        Find the XXX companies with the largest market cap for the a given time (month within a year)

    INPUT SIGNATURE:
        1. number (int): top 500? top 100?
        2. date (list): [year, month]
        3. dataframe (Pandas dataframe): the source of our data, usually nasdaq_df

    OUTPUT SIGNATURE:
        1. largest_XXX (list): a list contains tickers of those XXX companies sorted alphabetically
    """

    # list to populate and return
    largest_XXX = []

    # our market
    sorted_market_df = calculate_market_values(date, dataframe)

    # get the 500 most valuable companies
    for row in range(number):
        ticker = sorted_market_df["Ticker"].iloc[row]
        largest_XXX.append(ticker)

    return largest_XXX

#------------------------------

def date_incrementor(start_date, end_date):
    """
    DESCRIPTION:
        Help increment up a month and check whether the start_date is matched with the end date or not

    INPUT SIGNATURE:
        1. start_date (list): [year, month]
        2. end_date (list): [year, month]

    OUTPUT SIGNATURE:
        1. next_month (list): [year, month]
        2. if start_date == end_date, return True
    """

    if start_date == end_date:
        return True

    # create the variable to return
    next_month = []
    
    # store values so that they are readable
    start_year = start_date[0]
    start_month = start_date[1]
    end_year = end_date[0]
    end_month = end_date[1]

    if start_month == 12:
        next_month.append(start_year + 1)
        next_month.append(1)

    else:
        next_month.append(start_year)
        next_month.append(start_month + 1)

    return next_month

    