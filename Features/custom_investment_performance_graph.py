# setting path to the directory with the features
import sys
sys.path.append(sys.path[0]+'/./Features')

# UNIVERSAL IMPORT
from universal_import import *

# import other features
import helper
import strategies_helper
import portfolio_class

# read the database
nasdaq_df = helper.get_dataframe()

#------------------------------

def juxtapose_portfolio(portfolio_ROI_df):
    """
    DESCRIPTION:
        Generate a graph (either bar or line) that juxtapose the user's custom portfolio against the SP100 and the monkey portfolio.

    INPUT SIGNATURE:
        1. portfolio_ROI_df (Pandas dataframe): the dataframe with 2 columns (Year, ROI) of the user's portfolio
            This dataframe can be generated with the method get_yearly_ROI() within the portfolio class

    OUTPUT SIGNATURE:
        1. The graph as a png store within the Internal Data folder
    """

    # get the SP100 and monkey investment dataframe
    SP100_df = pd.read_csv("Internal Data/SP100_yearly_ROI.csv")
    monkey_df = pd.read_csv("Internal Data/monkey_yearly_ROI.csv")

    # graph the figure
    fig, custom_portfolio = plt.subplots()

    # overlaying 3 line graphs onto each other
    custom_portfolio = sns.lineplot(x = 'Year', y = 'ROI', data = SP100_df) # first, the SP100 graph
    custom_portfolio = sns.lineplot(x = 'Year', y = 'ROI', data = monkey_df) # second, the monkey graph
    custom_portfolio = sns.lineplot(x = 'Year', y = 'ROI', data = portfolio_ROI_df) # third, the user's portfolio

#------------------------------

