# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

from flask import render_template, Flask, request
import pandas as pd

import sys
sys.path.append('Features')
from inspect_stock import *
from basic_stock_stat import *
from stock_ROI import *
from helper import *

app = Flask(__name__)

#------------------------------

# read in pandas dataframe
nasdaq_df = pd.read_csv("Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
nasdaq_df["Date"] = pd.to_datetime(nasdaq_df["Date"])

#------------------------------

@app.route("/")
def homepage():
    return render_template('nguyen_simple_input.html')

#------------------------------

@app.route("/stock_ROI")
def stock_ROI():
    """
    DESCRIPTION:
        This is the back-end of the stock_ROI page.

    INPUT SIGNATURE:
        1. ticker (string): the user only need to input a ticker

    OUTPUT SIGNATURE:
        1. graph: generate a graph visualizing the stock's ROI overtime
    """

    # ticker of the requested stock
    ticker = request.args["ticker"]

    

if __name__ == '__main__':
     app.run()