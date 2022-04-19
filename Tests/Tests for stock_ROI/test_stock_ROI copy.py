import unittest

import argparse
import pandas as pd

import path
import sys
# current
directory = path.Path(__file__).abspath()
  
# setting path to the directory with the feature
sys.path.append(directory.parent.parent.parent)

# importing the functions we are testing
from stock_ROI import *
from inspect_stock import check_query

# specifying path to test data
data_file = "../test_data_fabricated.csv"

