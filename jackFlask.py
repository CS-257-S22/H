from flask import Flask, render_template
import sys
sys.dont_write_bytecode = True
sys.path.append('../H/Features')
from basic_stock_stat import get_nasdaqDates
from helper import check_basicTicker

app = Flask(__name__)

@app.route('/')
def home():
    return "Jack's basic flask app. Enter a ticker symbol in the url to find out if it is or is not in the dataset. Format /isIn/(ticker)"

@app.route('/isIn/<ticker>')
def isIn(ticker):
    truefalse = check_basicTicker(ticker)
    if truefalse:
        return "The ticker " + ticker + " is in the dataset"
    else:
        return "The ticker " + ticker + " is NOT in the dataset"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)