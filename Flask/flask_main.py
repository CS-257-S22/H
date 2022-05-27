# setting path to the directory with the features
import sys
sys.path.append(sys.path[0]+'/../Features')

# UNIVERSAL IMPORT
from universal_import import *

# import other features
import inspect_stock
import basic_stock_stat
import stock_ROI
import helper

app = Flask(__name__)

#------------------------------

# read in pandas dataframe
nasdaq_df = helper.get_dataframe()

#------------------------------

@app.route("/")
def homepage():
    """
    DESCRIPTION:
        Default homepage route which displays information on the functionality of our website and displays search bars for the 
        basic data and stock ROI functions
    
    INPUT SIGNATURE:
        1. None

    OUTPUT SIGNATURE:
        1. Dynamically generate a homepage based on the given HTML and CSS file
    """
    return render_template('index_mainpage.html', tickers = helper.all_tickers())

#------------------------------

@app.route("/basicData", methods=['GET', 'POST'])
def basicData():
    """
    DESCRIPTION:
        This route displays basic data of a inputted stock including data on the earliest and latest days recorded as well as the days
        where the maximum and minimum values were recorded

    INPUT SIGNATURE:
        1. ticker (string): a ticker symbol which is passed in through a search bar from the homepage

    OUTPUT SIGNATURE:
        A dynamically generated site displaying
            1. A stock's statistics the earliest recorded date (Open, Close, Low, High, and Volume)
            2. A stock's statistics the latest recorded date (Open, Close, Low, High, and Volume)
            3. A stock's maximum price and the days which it occured
            4. A stock's minimum price and the days which it occured
    """
    ticker = request.form['ticker']
    dates = basic_stock_stat.get_dates(ticker)
    reformatedDates = str(int(dates[0][0])) + "-" + str(int(dates[0][1])) + "-" + str(int(dates[0][2])), str(int(dates[1][0])) + "-" + str(int(dates[1][1])) + "-" + str(int(dates[1][2]))
    data = helper.get_dataframe()
    extDates = basic_stock_stat.stock_extreme_dates(ticker, data)
    max = helper.get_max(ticker)
    min = helper.get_min(ticker)
    # max = str(int(extDates[0][0])) + "-" + str(int(extDates[0][1])) + "-" + str(int(extDates[0][2]))
    # min = str(int(extDates[1][0])) + "-" + str(int(extDates[1][1])) + "-" + str(int(extDates[1][2]))

    earliestData = inspect_stock.inspect(ticker, dates[0], "Low", nasdaq_df),\
        inspect_stock.inspect(ticker, dates[0], "High", nasdaq_df),\
        inspect_stock.inspect(ticker, dates[0], "Open", nasdaq_df),\
        inspect_stock.inspect(ticker, dates[0], "Close", nasdaq_df),\
        inspect_stock.inspect(ticker, dates[0], "Volume", nasdaq_df)
    latestData = inspect_stock.inspect(ticker, dates[1], "Low", nasdaq_df),\
        inspect_stock.inspect(ticker, dates[1], "High", nasdaq_df),\
        inspect_stock.inspect(ticker, dates[1], "Open", nasdaq_df),\
        inspect_stock.inspect(ticker, dates[1], "Close", nasdaq_df),\
        inspect_stock.inspect(ticker, dates[1], "Volume", nasdaq_df)

    return render_template("basicData.html", basicTicker=ticker,\
        earlyDate=reformatedDates[0],\
        lateDate=reformatedDates[1],\
        max=max[0], maxDay=max[1],\
        min=min[0], minDay=min[1],\
        earlyLow=earliestData[0],\
        earlyHigh=earliestData[1],\
        earlyOpen=earliestData[2],\
        earlyClose=earliestData[3],\
        earlyVolume=earliestData[4],\
        lateLow=latestData[0],\
        lateHigh=latestData[1],\
        lateOpen=latestData[2],\
        lateClose=latestData[3],\
        lateVolume=latestData[4])

#------------------------------

@app.route("/stock_ROI")
def graph_stock_ROI():
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
    graph = stock_ROI.graph_ROIs_over_time_one_stock(ticker, nasdaq_df)

    # get the proper path
    graph_url = url_for('static', filename = "photos/graphs/" + graph)
    # graph_location = "../../static/photos/" + graph

    # display the webpage that contains the graph
    return render_template("stock_ROI_graph.html", ticker = ticker, graph_image = graph_url)

#------------------------------

@app.route("/mock_portfolio")
def portfolio_menu():
    """
    DESCRIPTION:
        This is the men for the mock stock portfolio feature.
    INPUT SIGNATURE:
        1. None
    OUTPUT SIGNATURE:
        1. Dynamically generate a menu page based on the given HTML and CSS file
    """
return render_template("custom_portfolio.html")

#------------------------------

@app.errorhandler(404)
def page_not_found(e):
    """
        Description:
            A page to instruct the user on the steps to follow if an invalid route is entered.
        Returns:
            1. Render the 404 page based on an HTML file
    """

    # render the webpage
    return render_template("404.html")

#------------------------------

@app.errorhandler(500)
def python_bug(e):
    """
    Description:
        A page notifying the user that the encountered error is from the server, not the user.
    Returns:
        message500 -    a string informing the user that the error is from the server and it is not
                        their fault and tells them to inform the developement team 
    """

    # render the 500 error page
    return render_template("500.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 2727)
