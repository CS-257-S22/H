def inspect(date_to_find, securities, query_stat):
    # authors: Miles, Nguyen

    prices_df = pd.read_excel("Data/stock_prices.xlsx") # require import pandas as pd in the main program
    
    return prices_df.loc[(prices_df['Date'] == date_to_find) & (prices_df['SecuritiesCode'] == securities), query_stat]