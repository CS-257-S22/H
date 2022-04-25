# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

import flask
import pandas as pd

import sys
sys.path.append('Features')
from inspect_stock import *
from basic_stock_stat import *
from stock_ROI import *

app = flask.Flask(__name__)

#------------------------------

# read in pandas dataframe
nasdaq_df = pd.read_csv("Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
nasdaq_df["Date"] = pd.to_datetime(nasdaq_df["Date"])

#------------------------------

@app.route("/")
def homepage():
    """
    Create a homepage for the beta website.
    """

    header = "INVEST.ED BETA PLATFORM"
    home = "From here, you can navigate using the following routes to use the corresponding functions\n\n\
            1. Inspect a stock\n\
                * Route: /inspect_stock/[ticker symbol]/[year]/[month]/[statistic]\n\
                * Example: /inspect_stock/AAPL/2022/3/Open\n\n\
            2. Find the earliest and latest recorded dates of a stock in our database\n\
                * Route: /extreme_dates/[ticker symbol]\n\
                * Example: /extreme_dates/MSFT\n\n\
            3. Find the ROI of any stock (in percentage)\n\
                * Route: /stock_ROI/[ticker symbol]/[investment year]/[investment month]/[buying price]\
                    /[divestment year]/[divestment month]/[selling price]\n\
                * Example: stock_ROI/AMZN/2011/12/Low/2022/3/High\n"

    home2 = home.replace('\n', '<br>')

    return flask.render_template('invested_beta_template.html',\
        header1 = header,\
        title = "Invest.Ed Beta Platform",\
        text1 = home2)

#------------------------------

@app.route("/stock_ROI/<ticker_symbol>/<investment_year>/<investment_month>/<buying_price>/<divestment_year>/<divestment_month>/<selling_price>")
def flask_stock_ROI(ticker_symbol, investment_year, investment_month, buying_price,\
    divestment_year, divestment_month, selling_price):
    "DESCRIPTION:\
        This function is the web-interface of our stock_ROI feature.\
        It displays to the user what is their return on investment in percentage value."

    # convert input into the appropriate data format
    investment_year = int(investment_year)
    investment_month = int(investment_month)
    divestment_year = int(divestment_year)
    divestment_month = int(divestment_month)

    # convert the date variables into the appropriate data structure
    date_invest = [investment_year, investment_month]
    date_divest = [divestment_year, divestment_month]

    # calculate the ROI
    ROI = main_stock_ROI(ticker_symbol, date_invest, date_divest, buying_price, selling_price)

    # if there is no error
    if isinstance(ROI, float) == True:

        # message to display
        message_stock_ROI = "You invested in " + ticker_symbol +\
            "\nfrom " + str(investment_year) + "/" + str(investment_month) + " at " + buying_price +\
            "\nto " + str(divestment_year) + "/" + str(divestment_month) + " at " + selling_price +\
            "\n\n" +\
            "Your ROI (%): " + str(ROI)

        # convert message to html-friendly format
        message_stock_ROI = message_stock_ROI.replace("\n", "<br>")

    # we encountered an error
    else:

        # pass on the error
        message_stock_ROI = ROI

    return message_stock_ROI

#------------------------------

@app.route('/extreme_dates/<ticker>', strict_slashes=False)
def get_dates_of_stock(ticker):
    """
    This function calls on the function in basic_stock_stat.py, which is our second feature that returns the earliest and 
    latest dates of the stock specified by the ticker symbol parameter. The function takes in a ticker variable and 
    returns the dates for the stock that the ticker symbol belongs to. It also calls a helper function to handle
    the error of a ticker symbol not belonging in our dataset, and will return the error statement of what the helper
    function will return.
    """
    if not check_ticker(str(ticker), "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv"):
        return str(get_dates(str(ticker), "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv"))
        # return page_not_found(not check_ticker(str(ticker), "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv"))"
    result = str(get_dates(str(ticker), "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv"))
    return "The dates for " + str(ticker) + " are " + result

#------------------------------

@app.errorhandler(404)
def page_not_found(e):
    "A page to instruct the user for the continuous step if an invalid route is entered."

    # the message to be displayed
    message404 = "ERROR 404\n\nInvalid route.\nReturn to Home Page for more instruction. (i.e. You can use the Back button.)"

    # convert the message to html-friendly format
    message404 = message404.replace('\n', '<br>')

    # return the message
    return message404

#------------------------------

@app.route('/inspect_stock/<ticker>/<year>/<month>/<query_stat>', strict_slashes=False)
def inspect_specifified_stock(ticker,year,month,query_stat):
    """Returns a stock statistic based on input stock information or returns an invalid input message for invalid inputs """
    value = find_query(5, str(ticker), int(year), int(month), str(query_stat), "./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv", nasdaq_df)
    description = ""
    if not isinstance(value,str) :
        #checks to see if output is not an invalid input message
        description = str(ticker) + "'s " + str(query_stat) + " on " + str(month) + "/" + str(year) + ": "
    return description + str(value)

#------------------------------

@app.errorhandler(500)
def python_bug(e):
    "A page notifying the user that the encountered error is from the server, not the user."

    # the message to be displayed
    message500 =  "ERROR 500: INTERNAL SERVER ERROR\n\nDon't panic, it's NOT your fault!\n\
    The error is on the server's end. Please report it to the administrator for a patch.\n\n\
    We thank you kindly,\n\
    Invest.Ed Development Team"

    # convert the message to html-friendly format
    message500 = message500.replace("\n", "<br>")

    # return the message
    return message500

if __name__ == "__main__":
    app.run()