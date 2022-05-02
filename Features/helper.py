# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True
import pandas as pd

import csv

def check_basicTicker(ticker):
    """ 
    Runs our check_ticker method with preset dataset instead of taking one is as a parameter

    Input:
    Takes in the ticker symbol of the company you are looking for

    Output:
    Returns the result of check_ticker(ticker, fileName) where fileName is preset to a default file, essentially runs
    check_ticker on a preset datset instead of having to input as a parameter
    """
    return check_ticker(ticker, "Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")

def check_ticker(ticker, fileName):
    """This method ensures that the ticker parameter is located within our dataset and is thus a valid ticker symbol

    Input: A requested ticker symbol that we are trying to identify whether or not it is in the dataset. fileName which is the location of the file which 
    we want to check whether or requested ticker is located within.

    Output: A boolean representing whether or not the requested ticker symbol is found within the refreneced dataset   
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
    Objective:
    Helper function for reading the dataset to avoid multiple layers of abstraction

    Input:
    Takes in the directory location of a desired dataset

    Output: 
    Dataset ready for use in command line functions shaped by pandas

    """
    nasdaq_df = pd.read_csv(fileName)
    nasdaq_df["Date"] = pd.to_datetime(nasdaq_df["Date"])
    return nasdaq_df