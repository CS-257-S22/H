from flask import Flask
import sys
import pandas as pd

import path
# current directory
directory = path.Path(__file__).abspath()
# setting path to the directory with the feature
sys.path.append(directory.parent.parent)
sys.path.append("Features")
from inspect_stock import find_query, get_fileName


app = Flask(__name__)

@app.route('/')
def hello_user():
    return 'Hello User! Input in the link after the "/" the ticker symbol, year, month, and query you want to find.'


@app.route('/<ticker>/<year>/<month>/<query>', strict_slashes=False)
def get_query(ticker, year, month, query):
    fileName = get_fileName()
    result = find_query(5, str(ticker), int(year), int(month), str(query), "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv", fileName)
    # return "The " + str(query) + " price for " + str(ticker) + " during the " + str(month) + "month and " + str(year) + " is " + result
    return "The " + str(query) + " price for " + str(ticker) + " during month " + str(month) + " and year " + str(year) + " is " + str(result)


app.run(host='0.0.0.0', port=81)


if __name__ == '__main__':
    app.run()

