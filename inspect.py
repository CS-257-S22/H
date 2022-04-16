from winreg import QueryInfoKey


def terminal_input_for_basic_stock_stat():
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

    return ticker, [date_year, date_month], query_stat # dataformat: string

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