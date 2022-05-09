import csv

"""
flaskFunctions.py is a helper file for jackWebsite.py. This file contains a series of methods to
return some basic information about an inputted ticker symbol (Note as it's implemented right 
now it will only accept 'TSLA' as a valid ticker symbol).
"""

def getDates(ticker):
    """
    Objective: Return basic, hard coded, information about a inputted stock
    Input: Takes in a ticker symbol which must be recorded in our dataset (Only TSLA is acceptable at this time)
    Returns: The earliest and latest recorded dates of a particular stock (Only TSLA is acceptable at this time)
    """
    
    if (ticker == "TSLA"):
        return ["2015-10-16", "2020-08-13"]
    return "Invalid Ticker"

def getMax(ticker):
    """
    Objective: Searches through a dataset (Only data on TSLA is recorded at this time so it is hardcoded) and returns
    the maximum recorded 'High' price for a particular stock (Only TSLA is acceptable at this time). Also returns the
    data of the highest recorded stock price.
    Input: Takes in a ticker symbol which must be recorded in our dataset (Only TSLA is acceptable at this time)
    Output: The maximum recorded value of particular stock and the date it was recorded on
    """
    if (ticker == "TSLA"):
        stat = float(0)
        maxDate = ""
        f = open("./IndividualFlaskFrontEnd/tslaData.csv", 'r', encoding = "UTF-8")
        with f as rFile:
            reader = csv.reader(rFile, delimiter=",")
            next(reader)
            for item in reader:
                if (float(item[7]) > stat):
                    stat = float(item[7])
                    maxDate = item[0]
        f.close
        return stat, maxDate

    return "Please enter a valid ticker"

def getMin(ticker):
    """
    Objective: Searches through a dataset (Only data on TSLA is recorded at this time so it is hardcoded) and returns
    the minimum recorded 'Low' price for a particular stock (Only TSLA is acceptable at this time). Also returns the
    data of the lowest recorded stock price.
    Input: Takes in a ticker symbol which must be recorded in our dataset (Only TSLA is acceptable at this time)
    Output: The minimum recorded value of particular stock and the date it was recorded on
    """
    if (ticker == "TSLA"):
        stat = float(99999999999999999)
        minDate = ""
        f = open("./IndividualFlaskFrontEnd/tslaData.csv", 'r', encoding = "UTF-8")
        with f as rFile:
            reader = csv.reader(rFile, delimiter=",")
            next(reader)
            for item in reader:
                if (float(item[7]) < stat):
                    stat = float(item[7])
                    minDate = item[0]
        f.close
        return stat, minDate

    return "Please enter a valid ticker"
        
    
if __name__ == "__main__":
    print(getMin("TSLA"))
