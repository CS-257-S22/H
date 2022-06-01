# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

import pandas as pd
from stock_ROI import *
from helper import *
from inspect_stock import *

# get our dataframe from the PSQL database
nasdaq_df = get_dataframe()