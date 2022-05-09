# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

import pandas as pd

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
    return check_ticker(ticker, "Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")

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
            if row[10] == ticker:
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

def all_tickers(filePath = "../Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv"):

    """
    DESCRIPTION:
        Find all ticker symbols (without duplicates) in any dataset

    INPUT SIGNATURE:
        1. filePath (string): the path to our dataframe

    OUTPUT SIGNATURE
        1. all_tickers (list): a Python list contains all tickers (unordered)
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
    all_tickers = list(set(all_tickers))

    return all_tickers