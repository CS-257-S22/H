def terminal_input_for_basic_stock_stat():
    # authors: Geoffrey, Jack

    # write your code here

    # call terminal_input_for_basic_stock_stat
    # build a prompt that pops up to


    return ticker # dataformat: string

# ----------------------------

def basic_stock_stat(ticker, dataframe):
    """
    Find the earliest and latest record dates of a stock.

    Input Signature:
        1. ticker symbol (string)

    Output Signature:
        1. list [earliest year in record, earliest month in record]
        2. list [latest year in record, latest month in record]
    """

    # find the earliest dates
    earliest_date = find_earliest_or_latest_record(ticker, method = "earliest", dataframe = dataframe)

    # find the latest dates
    latest_date = find_earliest_or_latest_record(ticker, method = "latest", dataframe = dataframe)

    return earliest_date, latest_dateg

# ----------------------------

def find_earliest_or_latest_record(ticker, method, dataframe):


    if method == "earliest":

        # find the earliest year
        earliest_year = dataframe.loc[dataframe["Ticker Symbol"] == ticker]\
            ["Year"].min()

        # find the earliest month
        earliest_month = dataframe.loc[(dataframe["Ticker Symbol"] == ticker) &\
            (dataframe["Year"] == earliest_year)]\
            ["Month"].min()

        return [earliest_year, earliest_month]


    elif method == "latest":

        # find the latest year
        latest_year = dataframe.loc[dataframe["Ticker Symbol"] == ticker]\
            ["Year"].max()

        # find the latest month
        latest_month = dataframe.loc[(dataframe["Ticker Symbol"] == ticker) &\
            (dataframe["Year"] == earliest_year)]\
            ["Month"].max()

        return [latest_year, latest_month]