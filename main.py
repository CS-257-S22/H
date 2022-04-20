# import all libraries
import pandas as pd
import unittest
import argparse
import pandas as pd
import path
import sys
import csv

# import all sub-functions from other .py files
from inspect_stock import *

# read all available data
nasdaq_df = pd.read_csv("Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
nasdaq_df["Date"] = pd.to_datetime(nasdaq_df["Date"])

find_query(nasdaq_df)
