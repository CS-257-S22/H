from flask import *
app = Flask(__name__)

#Creates data frame based off of the stock data
import pandas as pd
nasdaq_df = pd.read_csv("./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")

#Creates file path to the Features directory and imports all features
import sys
sys.path.append('./Features')
from inspect_stock import *
from basic_stock_stat import *
from stock_ROI import *

@app.route('/')
def homepage():
    """Returns a greeting to the user and information on how to use the inspect route"""
    return "Welcome to our flask app!"

@app.route('/inspect_stock/<ticker>/<year>/<month>/<query_stat>', strict_slashes=False)
def inspect_specifified_stock(ticker,year,month,query_stat):
    """Returns a stock statistic based on input stock information or returns an invalid input message for invalid inputs """
    value = find_query(5, str(ticker), int(year), int(month), str(query_stat), "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv", nasdaq_df)
    description = ""
    if not isinstance(value,str) :
        #checks to see if output is not an invalid input message
        description = str(ticker) + "'s " + str(query_stat) + " on " + str(month) + "/" + str(year) + ": "
    return description + str(value)


@app.errorhandler(404)
def page_not_found(e):
    """Returns a statement informing the user that they input the route/parameters incorrectly and informs them of the propper format"""
    return "Sorry, wrong format"

@app.errorhandler(500)
def python_bug(e):
    return "Eek, a bug!"


if __name__ == '__main__':
    app.run()
