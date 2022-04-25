# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

import flask
import pandas as pd

import sys
sys.path.append('Flask')
from Flask_App_main import *

import unittest

class test_Flask_stock_ROI(unittest.TestCase):

    def test_route(self):
        """
        Flask app for stock_ROI integration test
            This method does 5 tests for the ability of the Flask app for stock_ROI to integrate all of the underlying functions
            and produce the appropriate result to the user.
        """

        self.app = app.test_client()

        # list of inputs for testing purposes
        given = [["AMD", [2017, 3] , [2022, 3], "Low", "High"],\
            ["RIBT", [2010, 3], [2022, 3], "Open", "High"],\
            ["GENE", [2017, 11], [2022, 3], "Open", "Close"],\
            ["HWBK", [2012, 2], [2022, 3], "High", "Open"],\
            ["SAFM", [2017, 9], [2022, 3], "Close", "Low"]]

        # convert the list of inputs into routes
        routes = route_generator_stock_ROI(given)

        # list of corresponding expected output
        expected = [705.3597897435196,\
            -97.38888889551163,\
            -42.18750011641532,\
            287.1387238256577,\
            11.231881260542963]

        # loop through all the possible routes/input and compare the result
        for i in range(len(routes)):

            # get the Flask app output
            response = self.app.get(routes[i], follow_redirects=True)

            # our expected output
            ROI = expected[i]

            # our output message
            message_stock_ROI = "You invested in " + given[i][0] +\
                "\nfrom " + str(given[i][1][0]) + "/" + str(given[i][1][1]) + " at " + given[i][3] +\
                "\nto " + str(given[i][2][0]) + "/" + str(given[i][2][1]) + " at " + given[i][4] +\
                "\n\n" +\
                "Your ROI (%): " + str(ROI)

            message_stock_ROI = message_stock_ROI.replace("\n", "<br>")

            # comparing the output to the expected
            self.assertEqual(bytes(message_stock_ROI, encoding='utf-8'), response.data)

    #------------------------------

    def test_route_edge(self):
        """
        Flask app for stock_ROI's edge cases test
            This method does 2 tests at 2 ends of our data
            for the ability of the Flask app for stock_ROI to integrate all of the underlying functions
            and produce the appropriate result to the user.
        """

        self.app = app.test_client()

        # list of inputs for testing purposes
        given = [["ZUMZ", [2010, 1] , [2022, 3], "Low", "High"],\
            ["AAL", [2010, 1], [2022, 3], "Open", "High"]]

        # convert the list of inputs into routes
        routes = route_generator_stock_ROI(given)

        # list of corresponding expected output
        expected = [207.3442263507863, 180.1418539851878]

        # loop through all the possible routes/input and compare the result
        for i in range(len(routes)):

            # get the Flask app output
            response = self.app.get(routes[i], follow_redirects=True)

            # our expected output
            ROI = expected[i]

            # our output message
            message_stock_ROI = "You invested in " + given[i][0] +\
                "\nfrom " + str(given[i][1][0]) + "/" + str(given[i][1][1]) + " at " + given[i][3] +\
                "\nto " + str(given[i][2][0]) + "/" + str(given[i][2][1]) + " at " + given[i][4] +\
                "\n\n" +\
                "Your ROI (%): " + str(ROI)

            message_stock_ROI = message_stock_ROI.replace("\n", "<br>")

            # comparing the output to the expected
            self.assertEqual(bytes(message_stock_ROI, encoding='utf-8'), response.data)


    #------------------------------

    def test_validity_of_inputs(self):
        """
        Flask app for stock_ROI unit test
            Test how the app handles invalid inputs
        """
        
        self.app = app.test_client()

        # list of inputs for testing purposes
        given = [["GEne", [2017, 11], [2022, 6], "Open", "Close"],\
            ["HWBK", [2099, 2], [2022, 8], "Adjusted Close", "Open"],\
            ["SAFM", [2017, 9], [2022, 3], "Baka", "Low"]]

        # list of corresponding expected output
        expected = ["INPUT ERROR: Invalid ticker symbol. Please choose one that exists within our data instead.",\
            "INPUT ERROR: Invalid year for investment date.",\
            "INPUT ERROR: Invalid buying price. Choose between 'Open', 'Close', 'High', 'Close', and 'Adjusted Close' only."]

        # convert the list of inputs into routes
        routes = route_generator_stock_ROI(given)

        # loop through all the possible routes/input and compare the result
        for i in range(len(routes)):

            # get the Flask app output
            response = self.app.get(routes[i], follow_redirects=True)

            # our expected output
            validity = expected[i]

            # comparing the output to the expected
            self.assertEqual(bytes(validity, encoding='utf-8'), response.data)

#------------------------------

def route_generator_stock_ROI(input_list):
    """
    This helper function helps convert a list of complex inputs into a list of routes corresponding to each input
    that the Flask app can use.
    """

    routes = []

    for item in input_list:

        # separate the inputs into structural variables
        ticker = item[0]
        investment_year = item[1][0]
        investment_month = item[1][1]
        buying_price = item[3]
        divestment_year = item[2][0]
        divestment_month = item[2][1]
        selling_price = item[4]

        compiler = "/stock_ROI/" + ticker + "/" + str(investment_year) + "/" + str(investment_month) + "/" + buying_price +\
            "/" + str(divestment_year) + "/" + str(divestment_month) + "/" + selling_price

        routes.append(compiler)

    return routes

#------------------------------

if __name__ == '__main__':
    unittest.main()