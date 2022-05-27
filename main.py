# setting path to the directory with the features
import sys
sys.path.append(sys.path[0]+'/../Features')

# UNIVERSAL IMPORT
from universal_import import *

# import other features

from Features import inspect_stock, basic_stock_stat, stock_ROI, helper

# read all available data
nasdaq_df = helper.get_dataframe()

#------------------------------

def run_feature_called():
    """
    Objective:
    This function checks the user input for the command line app and runs the valid corresponding feature.

    Input Signature:

    First Argument: specifies which feature will be used
    -inspect: calls the inspect stock feature
    -basic_stat: calls the basic stock stat feature
    -stock_ROI: calls the stock ROI feature

    proceeding arguments for -inspect:
    ticker: this is the ticker symbol for the stock, ex. AAPL
    year: this is the specified year of the stock that the user wants to find, ex. 2021
    month: this is the specified month of the stock that the user wants to find, ex. 3
    query: This is the type of statistic that the user wants, ex. Open

    Output:
    The statistic (specified by the query input argument) of a stock (specified by ticker symbol)
    at a certain point in time (specified by month and year of investment).

    """
    num_of_args = len(sys.argv)
    if num_of_args == 1:
        print("No feature Input! Try using the arguments -inspect, -basic_stat, or -stock_ROI")
        return False
    
    feature = str(sys.argv[1])
    if feature == "-inspect":
        return inspect_stock.find_query_input()

    elif feature == "-basic_stat":
        return basic_stock_stat.get_dates_input()

    elif feature == "-stock_ROI":
        ticker = str(sys.argv[2])
        date_invest = [int(sys.argv[3]), int(sys.argv[4])]
        date_divest = [int(sys.argv[6]), int(sys.argv[7])]
        buying_price = str(sys.argv[5])
        selling_price = str(sys.argv[8])
        return stock_ROI.main_stock_ROI(ticker, date_invest, date_divest, buying_price, selling_price)
            

    else:
        return "Invalid feature! Try using the arguments -inspect, -basic_stat, or -stock_ROI"

if __name__ == '__main__':
    print(run_feature_called())