#Will remove the import in the future
import pandas as pd
import datetime

def inspect(date_to_find, securities, query_stat):
    # authors: Miles, Nguyen

    prices_df = pd.read_excel("Data/stock_prices.xlsx")
    
    return prices_df.loc[(prices_df['Date'] == date_to_find) & (prices_df['SecuritiesCode'] == securities), query_stat]