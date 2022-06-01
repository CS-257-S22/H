# setting path to the directory with the features
import sys
sys.path.append(sys.path[0]+'/./Features')

# UNIVERSAL IMPORT
from universal_import import *

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
    SP100_df = pd.read_csv("./Features/Internal Data/SP100_yearly_ROI.csv")
    monkey_df = pd.read_csv("./Features/Internal Data/monkey_yearly_ROI.csv")

    # graph the figure
    fig, custom_portfolio_graph = plt.subplots()

    # overlaying 3 line graphs onto each other
    custom_portfolio_graph = sns.lineplot(x = 'Year', y = 'ROI', color = "red", data = SP100_df) # first, the SP100 graph
    custom_portfolio_graph = sns.lineplot(x = 'Year', y = 'ROI', color = "green", data = monkey_df) # second, the monkey graph
    custom_portfolio_graph = sns.lineplot(x = 'Year', y = 'ROI', color = "blue", data = portfolio_ROI_df) # third, the user's portfolio
    plt.legend(labels=["SP100 Portfolio","Monkey Portfolio", "Custom Portfolio"])

    # generate graph's name and path
    name = "custom_portfolio_figure.png"
    location = "./Flask/static/photos/graphs/"
    final_path = location + name

    # export the graph
    custom_portfolio_graph.figure.savefig(final_path)
    custom_portfolio_graph.figure.clf()

    # return the name for accessibility from other functions
    return name

#------------------------------

