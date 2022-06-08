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

#------------------------------

@app.route("/")
def homepage():
    return render_template("nguyen_simple_input.html")

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