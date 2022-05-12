# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

from flask import render_template, Flask, request, url_for

import pandas as pd
import seaborn as sns
# set desired graph size
sns.set(rc={'figure.figsize':(15,10)})
# set background color
sns.set(rc={"axes.facecolor":"white", "figure.facecolor":"white"})

# attempting to fix NSWindow Drag Exception
import matplotlib
matplotlib.pyplot.switch_backend('Agg')

import sys
sys.path.append('Features')
from inspect_stock import *
from basic_stock_stat import *
from stock_ROI import *
from helper import *

app = Flask(__name__)

#------------------------------

# read in pandas dataframe
nasdaq_df = pd.read_csv("Data/Polished/randomized_day_market.csv")
nasdaq_df["Date"] = pd.to_datetime(nasdaq_df["Date"])

#------------------------------

@app.route("/")
def homepage():
    """
    Default homepage route which displays information on the functionality of our website and displays search bars for the 
    basic data and stock roi functions
    """
    return render_template('index_mainpage.html', tickers = all_tickers())

#------------------------------

@app.route("/basicData", methods=['GET', 'POST'])
def basicData():
    """
    Description: This route displays basic data of a inputted stock including data on the earliest and latest days recorded as well as the days
    where the maximum and minimum values were recorded

    Input: Takes in a ticker symbol which is passed in through a search bar from the homepage

    Output: Basic data on the requested stock including, the earliest and latest recorded dates of the stock including he low, high, open, close and volume of these dates.
    Also displays data regarding the days in which the maximum and minimum value of the stock was recorded.
    """
    ticker = request.form['ticker']
    dates = get_dates(ticker, "Data/Polished/randomized_day_market.csv")
    reformatedDates = str(dates[0][0]) + "-" + str(dates[0][1]) + "-" + str(dates[0][2]), str(dates[1][0]) + "-" + str(dates[1][1]) + "-" + str(dates[1][2])
    max = getMax(ticker)
    min = getMin(ticker)

    earliestData = inspect(ticker, dates[0], "Low", nasdaq_df), inspect(ticker, dates[0], "High", nasdaq_df), inspect(ticker, dates[0], "Open", nasdaq_df), inspect(ticker, dates[0], "Close", nasdaq_df), inspect(ticker, dates[0], "Volume", nasdaq_df)
    latestData = inspect(ticker, dates[1], "Low", nasdaq_df), inspect(ticker, dates[1], "High", nasdaq_df), inspect(ticker, dates[1], "Open", nasdaq_df), inspect(ticker, dates[1], "Close", nasdaq_df), inspect(ticker, dates[1], "Volume", nasdaq_df)
    return render_template("basicData.html", basicTicker=ticker, earlyDate=reformatedDates[0], lateDate=reformatedDates[1], max=max[0], maxDay=max[1], min=min[0], minDay=min[1], earlyLow=earliestData[0], earlyHigh=earliestData[1], earlyOpen=earliestData[2], earlyClose=earliestData[3], earlyVolume=earliestData[4], lateLow=latestData[0], lateHigh=latestData[1], lateOpen=latestData[2], lateClose=latestData[3], lateVolume=latestData[4])

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

    # generate the requested ticker's yearly ROI graph in the back-end
    graph = graph_ROIs_over_time_one_stock(ticker, nasdaq_df)

    # get the proper path
    graph_url = url_for('static', filename = "photos/graphs/" + graph)
    # graph_location = "../../static/photos/" + graph

    # display the webpage that contains the graph
    return render_template("stock_ROI_graph.html", ticker = ticker, graph_image = graph_url)

if __name__ == '__main__':
     app.run()
