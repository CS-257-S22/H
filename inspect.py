import sys
import csv
from winreg import QueryInfoKey

def find_query():
    num_of_args = len(sys.argv)
    ticker = sys.argv[0]
    year = sys.argv[1]
    month = sys.argv[2]
    query = sys.argv[3]
    if not check_num_args(num_of_args):
        print("There need to be 4 arguments; TickerSymbol, Year, Month, Query")
        return

    if not check_ticker(ticker):
        print("Ticker not found in dataset")
        return
    
    if not check_year(year):
        print("Year not in dataset")
        return
        
    if not check_month(month):
        print("Invalid month")
        return

    actual_ticker, actual_date, actual_query = inspect_input(num_of_args, ticker, year, month, query)
    inspect(actual_ticker, actual_date, actual_query, nasdaq_df)

def inspect_input(num_of_args, ticker, year, month, query):
    """
    Author:
        1. Jack
        2. Geoffrey

    Objective:
        1. Obtain user input from terminal

    Input Signature:
        1. None (pop-up prompt for user instead)

    Output Signature:
        1. ticker (string)
        2. list of [year of interested date (int64), month of interested date (int64)
        3. query_stat (string, "Open", "Close", "High", etc.)
    """

    return str(ticker), [str(sys.argv[1]), str(sys.argv[2])], str(sys.argv[3])

    #inspect.py --find_query tickersymbol year month query
    
    # return ticker, [date_year, date_month], query_stat # dataformat: string

def check_num_args(num_of_args):
    if num_of_args != 4:
        return False
    return True

def check_ticker(ticker):
    fileName = "NO_NULL_nasdaq_2010_mid_seperate_year_month_day.csv"
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
    
    
def check_year(year):
    if (2010 <= year <= 2022):
        return True
    return False

def check_month(month):
    if (1 <= month <= 12):
        return True
    return False
    
def check_query(query):
    list = ["Low", "Open", "Volume", "High", "Close", "AdjustedClose"]
    if query in list:
        return True
    return False

def inspect(date_to_find, securities, query_stat, prices_df):
    '''NEED TO BE REWRITTEN DUE TO NEW DATA'''

    prices_df = pd.read_excel("Data/stock_prices.xlsx") # require import pandas as pd in the main program
    
    return prices_df.loc[(prices_df['Date'] == date_to_find) & (prices_df['SecuritiesCode'] == securities), query_stat]