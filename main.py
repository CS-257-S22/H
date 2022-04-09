# import all libraries
import pandas as pd
import datetime
import random

# import all sub-functions from other .py files
from inspect import *
from sector_ROI import *

# read all available data
prices_df = pd.read_excel("Data/stock_prices.xlsx")
list_df = pd.read_excel("Data/stock_list_error_free.xlsx")

