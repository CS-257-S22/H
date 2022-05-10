# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

import pandas as pd
import path
# current directory
directory = path.Path(__file__).abspath()
# setting path to the directory with the feature
sys.path.append(directory.parent.parent)

import csv

def check_basicTicker(ticker):
    """
    Description:
        Runs our check_ticker method with preset dataset instead of taking one as a parameter

    Input:
        1. Ticker symbol of the company you are looking for

    Output:
        1. Returns the result of check_ticker(ticker, fileName) where fileName is preset to a default file
    """
    return check_ticker(ticker, "./Data/Polished/randomized_day_market.csv")

def check_ticker(ticker, fileName):
    """
    Description:
        1. Ensure that the ticker parameter is located within our dataset and is thus a valid ticker symbol

    Input:
        1. The requested ticker symbol that we are trying to identify whether or not it is in the dataset
        2. fileName which is the location of our dataset

    Output:
        1. A boolean representing whether or not the requested ticker symbol is found within the reference dataset   
    """
    
    f = open(fileName, 'r', encoding = "UTF-8")
    with f as rFile:
        spamreader = csv.reader(rFile, delimiter=',')
        next(spamreader)
        for row in spamreader:
            if row[9] == ticker:
                f.close
                return True
    f.close
    return False 

def get_dataframe(fileName):

    """
    Description:
        1. Helper function for reading the dataset to avoid multiple layers of abstraction

    Input:
        1. Path to the file of our dataset

    Output: 
        2. Dataset ready for use in command line functions shaped by pandas
    """

    nasdaq_df = pd.read_csv(fileName)
    nasdaq_df["Date"] = pd.to_datetime(nasdaq_df["Date"])
    return nasdaq_df


def getExtremeDates(ticker):
    if not check_ticker(ticker, "./Data/Polished/randomized_day_market.csv"):
        return "Please input a valid ticker symbol"
    f = open("./Data/Polished/randomized_day_market.csv", 'r', encoding = "UTF-8")
    firstDate = ""
    lastDate = ""
    with f as rFile:
        spamreader = csv.reader(rFile, delimiter=',')
        next(spamreader)
        for row in spamreader:
            if row[9] == ticker:
                firstDate = row[0]
                break
        for row in spamreader:
            if row[9] != ticker:
                lastDate = row[0]
                break
    f.close
    return firstDate, lastDate

def getMax(ticker):
    """
    Objective: Searches through a dataset (Only data on TSLA is recorded at this time so it is hardcoded) and returns
    the maximum recorded 'High' price for a particular stock (Only TSLA is acceptable at this time). Also returns the
    data of the highest recorded stock price.
    Input: Takes in a ticker symbol which must be recorded in our dataset (Only TSLA is acceptable at this time)
    Output: The maximum recorded value of particular stock and the date it was recorded on
    """
    if not check_ticker(ticker, "./Data/Polished/randomized_day_market.csv"):
        return "Please input a valid ticker symbol"
    stat = float(0)
    maxDate = ""
    f = open("./Data/Polished/randomized_day_market.csv", 'r', encoding = "UTF-8")
    with f as rFile:
        reader = csv.reader(rFile, delimiter=",")
        next(reader)
        for item in reader:
            if item[9] == ticker:
                if (float(item[7]) > stat):
                    stat = float(item[7])
                    maxDate = item[0]
    f.close
    return stat, maxDate

def getMin(ticker):
    """
    Objective: Searches through a dataset (Only data on TSLA is recorded at this time so it is hardcoded) and returns
    the maximum recorded 'High' price for a particular stock (Only TSLA is acceptable at this time). Also returns the
    data of the highest recorded stock price.
    Input: Takes in a ticker symbol which must be recorded in our dataset (Only TSLA is acceptable at this time)
    Output: The maximum recorded value of particular stock and the date it was recorded on
    """
    if not check_ticker(ticker, "./Data/Polished/randomized_day_market.csv"):
        return "Please input a valid ticker symbol"
    stat = float(99999999999999999)
    minDate = ""
    f = open("./Data/Polished/randomized_day_market.csv", 'r', encoding = "UTF-8")
    with f as rFile:
        reader = csv.reader(rFile, delimiter=",")
        next(reader)
        for item in reader:
            if item[9] == ticker:
                if (float(item[7]) < stat):
                    stat = float(item[7])
                    minDate = item[0]
    f.close
    return stat, minDate

def all_tickers(filePath = "./Data/Polished/randomized_day_market.csv"):

    """
    DESCRIPTION:
        Find all ticker symbols (without duplicates) in any dataset

    INPUT SIGNATURE:
        1. filePath (string): the path to our dataframe

    OUTPUT SIGNATURE
        1. all_tickers_not_duplicate (list): a Python list contains all tickers (unordered)
    """

    # read the data
    stock_df = pd.read_csv(filePath)

    # a list to store all tickers
    all_tickers = []

    # loop through the dataframe and get all tickers
    for i in range(len(stock_df)) :
        ticker = stock_df.loc[i, "Ticker Symbol"]
        all_tickers.append(ticker)

    # remove duplicate items
    all_tickers_not_duplicate = []
    
    for item in all_tickers:

        if item in all_tickers_not_duplicate:
            pass

        else:
            all_tickers_not_duplicate.append(item)

    return all_tickers_not_duplicate

