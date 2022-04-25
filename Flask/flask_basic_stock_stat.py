from flask import Flask
from flask import render_template
import sys
import pandas as pd

import path
# current directory
directory = path.Path(__file__).abspath()
# setting path to the directory with the feature
sys.path.append(directory.parent.parent)
sys.path.append("Features")
from inspect_stock import find_query, get_fileName
from helper import check_ticker
from basic_stock_stat import get_dates


app = Flask(__name__)

@app.route('/')
def hello_user():
    """
    This function is for the main page. It includes a html file for displaying the instructions of how to input route parameters
    to access information on our dataset. 
    """
    return "This is the main page!"
    # return render_template('index.html')


# @app.route('/<ticker>/<year>/<month>/<query>', strict_slashes=False)
# def get_query(ticker, year, month, query):
#     """
#     This function calls on the function in inspect_stock.py, which is our first feature for the command line interface.
#     It returns the price of the stock at the specified ticker symbol, date, and query. This function calls on that function
#     and returns the string result of what the command line function returns. 
#     """
#     fileName = get_fileName()
#     result = find_query(5, str(ticker), int(year), int(month), str(query), "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv", fileName)
#     return "The " + str(query) + " price for " + str(ticker) + " during month " + str(month) + " and year " + str(year) + " is " + str(result)

@app.route('/<ticker>', strict_slashes=False)
def get_dates_of_stock(ticker):
    """
    This function calls on the function in basic_stock_stat.py, which is our second feature that returns the earliest and 
    latest dates of the stock specified by the ticker symbol parameter. The function takes in a ticker variable and 
    returns the dates for the stock that the ticker symbol belongs to. It also calls a helper function to handle
    the error of a ticker symbol not belonging in our dataset, and will return the error statement of what the helper
    function will return.
    """
    if not check_ticker(str(ticker), "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv"):
        # return "Ticker not in dataset"
        return page_not_found(not check_ticker(str(ticker), "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv"))
    result = str(get_dates(str(ticker), "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv"))
    return "The dates for " + str(ticker) + " are " + result

@app.errorhandler(404)
def page_not_found(e):
    """
    This function is a helper function for errors regarding the ticker symbol. If the inputted ticker symbol is 
    not in the list then it will return a message indicating that they need to input a valid ticker symbol.
    """
    return "Ticker not in dataset. Please try inputting another ticker symbol instead"


app.run(host='0.0.0.0', port=80)


if __name__ == '__main__':
    app.run()

