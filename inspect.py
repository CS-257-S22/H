import sys
from winreg import QueryInfoKey


def terminal_input_for_inspect():
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
    num_of_args = len(sys.argv)
    ticker = sys.argv[0]
    year = sys.argv[1]
    month = sys.argv[2]
    query = sys.argv[3]

    if not check_num_args(num_of_args) or not check_ticker(ticker) or not check_year(year) or not check_month(month) or not check_query(query):
        #end function and print error
        return

    return str(ticker), [str(sys.argv[1]), str(sys.argv[2])], str(sys.argv[3])

    #inspect.py tickersymbol year month query
    
    return ticker
    , [date_year, date_month], query_stat # dataformat: string

def check_num_args(num_of_args):
    if num_of_args != 4:
        print('There need to be 4 arguments; TickerSymbol, Year, Month, Query')
        return False
    return True

def check_ticker(ticker):
    return 
    
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
    
    dataframe.loc[(dataframe['Ticker Symbol'] == ticker) & (dataframe['Year'] == date[0]) & (dataframe['Month'] == date[1]), query_stat]