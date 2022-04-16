import sys
import csv
import pandas as pd
import datetime

def find_query():

    nasdaq_df = pd.read_csv("Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
    nasdaq_df["Date"] = pd.to_datetime(nasdaq_df["Date"])

    num_of_args = len(sys.argv)
    ticker = sys.argv[0]
    year = sys.argv[1]
    month = sys.argv[2]
    query = sys.argv[3]

    print(num_of_args, ticker, year, month, query)

find_query()