# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

import pandas as pd
from stock_ROI import *
from helper import *
from inspect_stock import *

# get our dataframe from the PSQL database
nasdaq_df = get_dataframe()

class portfolio():

    def __init__(self):

        # the total value of the portfolio (be noted that our portfolio only support buying/selling ONE share per transaction)
        self.value = 0

        # the amount of cash in the portfolio
        self.liquid = 0

        # the amount of money invested (since the initialization of the portfolio)
        self.invested = 0

        # the amount of money gained from all selling
        self.divested = 0

        # the ROI of the portfolio (in percentage)
        self.ROI = 0

        # keep track of all attributes above yearly (basically store each year's attributes as an item in a list)
        self.yearly_dairy = []

        # dictionary storing our holdings in each company
        self.holdings = {} # {"AAPL:[210, 299, 444]"} each item the list represents a share bought by conveying the share's value

        # this class will record all interactions within the portfolio (each buy and sell transaction) in a Pandas dataframe
        # to create that dataframe, it will use a series of ordered lists
        self.ticker = []
        self.action = [] # buy or sell
        self.year = []
        self.month = []
        self.query = [] # low, high, open, close
        self.price = [] # the price at that query

        # the Pandas dataframe that keeps track of all interaction (this will be created and stored by a method)
        self.transaction_df = None

        # keeping track of whether the latest transaction is included in the tally or not (default True)
        self.latest_transaction_tally_state = True

    #------------------------------

    def tally(self):
        """
        DESCRIPTION:
            Store the complete Pandas dataframe will each transaction as a line to self.transaction_df
        """

        self.reset()

        data = {"Ticker":self.ticker, "Action":self.action, "Year":self.year, "Month":self.month, "Query":self.query, "Price":self.price}

        self.transaction_df = pd.DataFrame(data)

        # sort the dataframe by time (ascending)
        self.transaction_df.sort_values(['Year', 'Month'], ascending = [True, True])

        self.latest_transaction_tally_state = True

        return self.transaction_df

    #------------------------------

    def reset(self):
        """
        Reset the portfolio object to its default value, to ready for a new tally
        """

        # the total value of the portfolio (be noted that our portfolio only support buying/selling ONE share per transaction)
        self.value = 0

        # the amount of cash in the portfolio
        self.liquid = 0

        # the amount of money invested (since the initialization of the portfolio)
        self.invested = 0

        # the amount of money gained from all selling
        self.divested = 0

        # the ROI of the portfolio (in percentage)
        self.ROI = 0

        # dictionary storing our holdings in each company
        self.holdings = {} # {"AAPL:[210, 299, 444]"} each item the list represents a share bought by conveying the share's value

        # the Pandas dataframe that keeps track of all interaction (this will be created and stored by a method)
        self.transaction_df = None

    #------------------------------

    def transaction(self, ticker, action, date, query):
        """
        INPUT SIGNATURE:
            1. ticker (string)
            2. action (string): "BOUGHT" or "SOLD"
            2. date (list): [year, month]
            3. query (string): "Open", "Low", "Close", "High"
            Example: transaction("AAPL", "BOUGHT", [2012, 3], "Low")

        OUTPUT SIGNATURE:
            1. adjust the lists ticker, action, year, month, query, and price
            2. adjust self.invested and self.liquid to reflect how much money is invested, and how much money is still in cash form
        """

        # capitalized all letter within action variable just in case of human error
        action = action.upper()

        closest_record = closest_available_record(ticker, date, nasdaq_df)

        if closest_record == True:

            # find the price of the transaction
            price = inspect(ticker, date, query, nasdaq_df)

            # adjust the records
            self.ticker.append(ticker)
            self.action.append(action)
            self.year.append(date[0])
            self.month.append(date[1])
            self.query.append(query)
            self.price.append(price)

            # record that this transaction is not yet included in the tally
            self.latest_transaction_tally_state = False

        else:

            # do the transaction on the closest day
            price = inspect(ticker, closest_record, query, nasdaq_df)

            # adjust the records
            self.ticker.append(ticker)
            self.action.append(action)
            self.year.append(closest_record[0])
            self.month.append(closest_record[1])
            self.query.append(query)
            self.price.append(price)

            # record that this transaction is not yet included in the tally
            self.latest_transaction_tally_state = False

    #------------------------------

    def get_portfolio_value(self, year, month, query = "Close"):
        """
        DESCRIPTION
            Return the estimated value of the portfolio by supposedly liquidate all assesses at the query price
            on the last month (in the transaction_df) of the inputted year

        INPUT SIGNATURE:
            1. year (int): the year to estimate the value
            2. month (int): the month to estimate the value
            3. query (string): the price that the portfolio is supposedly liquidated at, default is Close

        OUTPUT SIGNATURE:
            1. self.value (float): the estimated value of the portfolio
            2. self.liquid (float): total cash amount in the brokerage account (starts from 0)
            3. self.invested (float): total money invested
            4. self.divested (float): total amount of money gained from divestment
            5. self.ROI (float): the ROI at this year (%)
        """

        # tally all transaction if necessary
        if self.latest_transaction_tally_state == False:
            self.tally()
        else:
            pass

        # always tally
        self.tally()

        # filter out up-to the year in question
        # to_this_year_df = self.transaction_df[self.transaction_df["Year"] <= year]
        to_this_year_df = self.transaction_df[self.transaction_df["Year"].apply(lambda x: x <= year)]

        # DEBUG
        print("\n\n\nLength of to_this_year_df after year filter:", len(to_this_year_df))

        # remove all entries in the same year BUT has larger month
        conditioning = to_this_year_df[(to_this_year_df["Year"] == year) & (to_this_year_df["Month"] > month)].index # is basically all the indices that needs to be dropped
        to_this_year_df.drop(conditioning, inplace = True)

        # DEBUG
        print("\n\nLength of to_this_year_df after conditioning filter:", len(to_this_year_df))

        # sort the data by Year, then Month
        to_this_year_df = to_this_year_df.sort_values(by = ["Year", "Month"])

        # reset the index
        to_this_year_df.reset_index(inplace = True)

        # DEBUG
        print("\n\nLength of to_this_year_df after sorting and resetting index:", len(to_this_year_df))

        # loop through the dataframe and calculate the value of the portfolio, the amount of money invested initially, and the amount in cash
        for row in range(len(to_this_year_df)):

            ticker = to_this_year_df.loc[row, "Ticker"]
            action = to_this_year_df.loc[row, "Action"]
            price = to_this_year_df.loc[row, "Price"]


            # adjust the record of how much is invested
            if action == "BOUGHT":

                self.liquid -= price
                self.invested += price

                # update the internal dictionary storing the holdings and values
                if ticker in self.holdings:
                    self.holdings[ticker].append(price) # add a new share and its price
                else:
                    self.holdings[ticker] = [price] # create a new list record 1 share

            elif action == "SOLD":

                self.liquid += price
                self.divested += price

                # update the internal dictionary storing the holdings and values
                if ticker in self.holdings:

                    # remove the share that has the highest value initially from holdings (to maximize ROI when calculating final_value/invested)
                    self.holdings[ticker].remove(max(self.holdings[ticker]))

                    # if all shares are sold, then remove the ticker as a key within the dictionary
                    if len(self.holdings[ticker]) == 0:
                        del self.holdings[ticker]

                else:
                    raise Exception("Cannot sell a stock that is not in the portfolio.")

            else:
                raise Exception("Only 'BOUGHT' or 'SOLD' is accepted for the 'action' parameter.")

        # calculate the value of the portfolio if all holdings are immediately liquidated
        # loops through all holdings and hypothetically liquidate them
        for firm in self.holdings:

            # the total amount of shares owned
            shares = len(self.holdings[firm])

            # DEBUG
            print("\n\n#------------------------------\n",\
                "Firm: ", firm,\
                "\nShares: ", shares)

            if shares == 0:
                raise Exception("Ticker not removed after selling all shares.")

            closest_record = closest_available_record(firm, [year, month], nasdaq_df)

            # DEBUG
            print("\nLiquidating: ",\
                firm,\
                "\nOn: ", year, "-", month,\
                "\nat: ", query)

            if closest_record == True:
                # the total cash equivalent of all owned shares
                liquitable = inspect(firm, [year, month], query, nasdaq_df) * shares

                self.value += liquitable

            else:
                # the total cash equivalent of all owned shares
                liquitable = inspect(firm, closest_record, query, nasdaq_df) * shares

                self.value += liquitable

        # calculate the ROI (in percentage)
        self.ROI = percentage_difference(self.invested, self.value)

        return self.value, self.liquid, self.invested, self.divested, self.ROI

    #------------------------------

    def get_yearly_ROI(self, divestment_year, write_csv = False):
        """
        WARNING:
            Potentially HUGE runtime

        DESCRIPTION:
            Calls get_portfolio_value() for every year until the input divestment_year
        
        INPUT SIGNATURE:
            1. divestment_year (int)

        OUTPUT SIGNATURE:
            1. Pandas dataframe with 2 columns: year and the corresponding ROI
            2. yearly_ROI_dict: a dictionary matching year:ROI
        """

        # tally all transaction if necessary
        if self.latest_transaction_tally_state == False:
            self.tally()
        else:
            pass

        earliest_year = self.get_earliest_date()[0]
        
        latest_month = 12 # this will change if the year reaches 2022, which we only have data until April

        # empty ordered list to store our values
        years = []
        correspond_ROI = []

        # loop through each year and get its ROI
        this_year = earliest_year

        # DEBUG
        print ("\n\nTHIS YEAR: ", this_year)

        while this_year != divestment_year:
            
            if this_year == 2022:
                latest_month = 4

            this_year_ROI = self.get_portfolio_value(this_year, latest_month)[-1]

            # record our data
            years.append(this_year)
            correspond_ROI.append(this_year_ROI)

            this_year += 1

        # get the last year ROI
        if divestment_year == 2022:
            latest_month = 4

        divestment_year_ROI = self.get_portfolio_value(divestment_year, latest_month)[-1]
        years.append(divestment_year)
        correspond_ROI.append(divestment_year_ROI)

        # create our Pandas dataframe
        data = {"Year":years, "ROI":correspond_ROI}
        yearly_ROI_df = pd.DataFrame(data)

        # write the dictionary
        yearly_ROI_dict = {}
        for i in range (len(years)):
            yearly_ROI_dict[years[i]] = correspond_ROI[i]

        # write the csv if requested
        # WARNING, THIS MIGHT OVERRIDE EXISTING CSV FILES WITH THE SAME NAME
        if write_csv == True:
            yearly_ROI_df.to_csv("Internal Data/yearly_ROI_from_portfolio_class.csv", index = False)


        return yearly_ROI_df, yearly_ROI_dict

    #------------------------------

    def get_earliest_date(self):
        """
        DESCRIPTION:
            Because user might add transactions to the portfolio in an unorderly manner, this function will return what is the
            earliest transaction, or the creation of the portfolio.

        OUTPUT SIGNATURE:
            1. Earliest date in the format [year, month] (Python list)
        """ 

        # tally all transaction if necessary
        if self.latest_transaction_tally_state == False:
            self.tally()
        else:
            pass

        earliest_year = self.transaction_df["Year"].iloc[0]
        earliest_month = self.transaction_df["Month"].iloc[0]

        return [earliest_year, earliest_month]

    #------------------------------

    def get_holdings(self, year):
        return self.holdings