import csv

def check_ticker(ticker):
    """This method ensures that the ticker parameter is located within our dataset and is thus a valid ticker symbol. Returns true if valid and false if invalid"""
    fileName = "Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv"
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