# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

import random

from helper import *
from portfolio_class import *
from strategies_helper import *

nasdaq_df = get_dataframe()

def SP100_yearly_new_method(investment_year, divestment_year, dataframe):
    """
    DESCRIPTION:
        Calculate the monthly ROIs of a portfolio that invests in the 500 companies with the largest market cap.
        Be noted that the list of these 500 companies are dynamically calculated and changed monthly.
    
    INPUT SIGNATURE:
        1. investment_year (int)
        2. divestment_year (int)
        3. dataframe (Pandas dataframe): the source of our data, usually nasdaq_df

    OUTPUT SIGNATURE:
        1. yearly_ROIs_time (dictionary): { "year-month" : [portfolio value, ROI (since the start of the portfolio)] }
            (first on the list, but will be returned last, index to this by using [-1])
        2. final_value (float): one of the final attribute of the porfolio on the divestment date
        3. final_liquid (float): like 2
        4. final_invested (float): like 2
        5. final_divested (float): like 2
        6. final_ROI (float percentage): like 2
    """

    # take into account for earliest and latest available data
    latest_month = 12

    if divestment_year == 2022:
        latest_month = 4

    # output dictionary
    yearly_ROIs = {}

    current_year = investment_year

    # list of all holdings within the portfolio updated monthly
    dynamic_holdings = []

    # create a portfolio object
    portfolio_SP100 = portfolio()

    while current_year != divestment_year:

        # get the monthly most valuable 500 companies
        yearly_largest_100 = theXXX(100, [current_year, 1], dataframe)

        # buy new companies that reaches the top 500 or reinvest in companies that stay in the top 500
        for firm in yearly_largest_100:

            portfolio_SP100.transaction(firm, "BOUGHT", [current_year, 1], "Close")
            dynamic_holdings.append(firm) # here, we actually wants to append a firm multiple times in case it fall off the top 500
            # then we will need to sell mulitple shares of said firm

        # to remove companies properly from the portfolio while not affecting the for loop
        # we will create a copy of the list and rewrite our holdings onto it while not record sold firms
        new_holdings = []

        # sell companies that lose the top 500 position
        for firm in dynamic_holdings:

            if firm in yearly_largest_100:
                new_holdings.append(firm)

            else:
                portfolio_SP100.transaction(firm, "SOLD", [current_year, 1], "Close")
                # we do NOT call new_holdings.append(firm) here

        # update new dynamic_holdings
        dynamic_holdings = new_holdings

        current_year += 1

    # yearly ROI
    return portfolio_SP100.get_yearly_ROI(divestment_year, write_csv = True)

yearly_ROI_df, yearly_ROI_dict = SP100_yearly_new_method(2020, 2022, nasdaq_df)

print("\n\n\n\nFINAL RESULT:\n")

print(yearly_ROI_dict)