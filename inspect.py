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

def inspect(date_to_find, securities, query_stat, prices_df):
    '''NEED TO BE REWRITTEN DUE TO NEW DATA'''

    prices_df = pd.read_excel("Data/stock_prices.xlsx") # require import pandas as pd in the main program
    
    return prices_df.loc[(prices_df['Date'] == date_to_find) & (prices_df['SecuritiesCode'] == securities), query_stat]