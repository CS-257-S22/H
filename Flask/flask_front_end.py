# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

from urllib import request
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
    return render_template('index_mainpage.html', tickers=all_tickers())

#------------------------------

@app.route("/basicData", methods =['GET', 'POST'])
def basicData():
    ticker = request.form['ticker']
    # dates = get_dates(ticker, "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
    dates = getExtremeDates(ticker)
    max = getMax(ticker)
    min = getMin(ticker)
    earliestData = inspect(ticker, str(dates[0]).split("-"), "Low", nasdaq_df), inspect(ticker, dates[0].split("-"), "High", nasdaq_df), inspect(ticker, dates[0].split("-"), nasdaq_df), inspect(ticker, dates[0].split("-"), "Close", nasdaq_df), inspect(ticker, dates[0].split("-"), "Volume", nasdaq_df)
    latestData = inspect(ticker, str(dates[1]).split("-"), "Low", nasdaq_df), inspect(ticker, dates[1].split("-"), "High", nasdaq_df), inspect(ticker, dates[1].split("-"), "Open", nasdaq_df), inspect(ticker, dates[1].split("-"), "Close", nasdaq_df), inspect(ticker, dates[1].split("-"), "Volume", nasdaq_df)
    return render_template("basicData.html", basicTicker=request.args['basicTicker'], earlyDate=dates[0], lateDate=dates[1], max=max[0], maxDay=max[1], min=min[0], minDay=min[1], earlyLow=earliestData[0], earlyHigh=earliestData[1], earlyOpen=earliestData[2], earlyClose=earliestData[3], earlyVolume=earliestData[4], lateLow=latestData[0], lateHigh=latestData[1], lateOpen=latestData[2], lateClose=latestData[3], lateVolume=latestData[4])

#------------------------------

@app.route("/stock_ROI")
def stock_ROI():
    pass

if __name__ == '__main__':
     app.run()