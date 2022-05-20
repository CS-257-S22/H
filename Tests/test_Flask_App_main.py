# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

import flask
import pandas as pd

import sys
sys.path.append('Flask')
from Flask_App_main import *

import unittest

class test_Flask_app(unittest.TestCase):

    def test_stock_ROI(self):
        """
        Flask app for stock_ROI integration test
            This method does 5 tests for the ability of the Flask app for stock_ROI to integrate all of the underlying functions
            and produce the appropriate result to the user.
        """

        self.app = app.test_client()

        # list of inputs for testing purposes
        given = [["AMD", [2017, 3] , [2022, 3], "Low", "High"],\
            ["RIBT", [2012, 3], [2022, 3], "Open", "High"],\
            ["GENE", [2017, 11], [2022, 3], "Open", "Close"],\
            ["HWBK", [2012, 2], [2022, 3], "High", "Open"],\
            ["SAFM", [2017, 9], [2022, 3], "Close", "Low"]]

        # convert the list of inputs into routes
        routes = route_generator_stock_ROI(given)

        # list of corresponding expected output
        expected = [699.0476190476189,\
            -98.11538457870483,\
            -41.26505762368915,\
            278.8730269264091,\
            12.236049408098589]

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

    def test_stock_ROI_edge(self):
        """
        Flask app for stock_ROI's edge cases test
            This method does 2 tests at 2 ends of our data
            for the ability of the Flask app for stock_ROI to integrate all of the underlying functions
            and produce the appropriate result to the user.
        """

        self.app = app.test_client()

        # list of inputs for testing purposes
        given = [["ZUMZ", [2012, 1] , [2022, 3], "Low", "High"],\
            ["AAL", [2012, 1], [2022, 3], "Open", "High"]]

        # convert the list of inputs into routes
        routes = route_generator_stock_ROI(given)

        # list of corresponding expected output
        expected = [49.705884974537206, 115.72103921641789]

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

    def test_route_case(self):
            """
            Tests that correct output is returned by the inspect_specified_stock function
            """
            self.app = app.test_client()
            response = self.app.get('/inspect_stock/NLST/2013/11/Volume', follow_redirects=True)
            self.assertEqual(b"NLST's Volume on 11/2013: 65700.0", response.data)

    #------------------------------
        
    def test_route_bad_ticker(self):
        """
        Tests that correct message is returned by the inspect_specified_stock function to inform the user that their ticker is invalid
        """
        self.app = app.test_client()
        response = self.app.get('/inspect_stock/AKJD/2013/11/Volume', follow_redirects=True)
        self.assertEqual(b"Ticker not found in dataset", response.data)

    #------------------------------

    def test_route_bad_date(self):
        """
        Tests that correct message is returned by the inspect_specified_stock function to inform the user that their date is invalid
        """
        self.app = app.test_client()
        response = self.app.get('/inspect_stock/HBP/2023/11/Open', follow_redirects=True)
        self.assertEqual(b"Invalid Date", response.data)

    #------------------------------

    def test_route_bad_query(self):
        """
        Tests that correct message is returned by the inspect_specified_stock function to inform the user that their input query stat is invalid
        """
        self.app = app.test_client()
        response = self.app.get('/inspect_stock/AAPL/2013/3/Date', follow_redirects=True)
        self.assertEqual(b"Invalid Query", response.data)

    #------------------------------

    def test_route_edge_beginning(self):
        """
        Tests that correct output is returned by the inspect_specified_stock function for first stock in the data set
        """
        self.app = app.test_client()
        response = self.app.get('/inspect_stock/AAL/2012/1/Low', follow_redirects=True)
        self.assertEqual(b"AAL's Low on 1/2012: 8.100000381469727", response.data)

    #------------------------------

    def test_route_edge_end(self):
        """
        Tests that correct output is returned by the inspect_specified_stock function for last stock in the data set
        """
        self.app = app.test_client()
        response = self.app.get('/inspect_stock/ZUMZ/2022/4/Close', follow_redirects=True)
        self.assertEqual(b"ZUMZ's Close on 4/2022: 38.790000915527344", response.data)

    #------------------------------

    def test_get_query(self):
        """
        This function is a route test for feature 2 of the flask app, which is basic_stock_stat. It specifies the 
        ticker symbol and checks to see if the function returns the correct dates for the stock on the page. 
        """
        self.app = app.test_client()
        response = self.app.get('/extreme_dates/FB', follow_redirects=True)
        self.assertEqual(b'The dates for FB are ([2012, 5, 29], [2022, 4, 1])', response.data)

    #------------------------------    

    def test_get_query_edge_1(self):
        """
        This function is an edge route test for feature 2 of the flask app. It specifies the 
        first ticker symbol of the dataset and checks to see if the function returns the correct 
        dates for the stock on the page.
        """
        self.app = app.test_client()
        response = self.app.get('/extreme_dates/AAL', follow_redirects=True)
        self.assertEqual(b'The dates for AAL are ([2012, 1, 31], [2022, 4, 1])', response.data)

    #------------------------------

    def test_get_query_edge_2(self):
        """
        This function is an edge route test for feature 2 of the flask app. It specifies the 
        last ticker symbol of the dataset and checks to see if the function returns the correct 
        dates for the stock on the page. 
        """
        self.app = app.test_client()
        response = self.app.get('/extreme_dates/ZUMZ', follow_redirects=True)
        self.assertEqual(b'The dates for ZUMZ are ([2012, 1, 9], [2022, 4, 4])', response.data)

    #------------------------------

    def test_get_query_integration(self):
        """
        This function is an integration route test for feature 2 of the flask app. It specifies 
        an incorrect ticker symbol of the dataset and checks to see if the function returns the correct 
        error message for the stock on the page.
        """
        self.app = app.test_client()
        response = self.app.get('/extreme_dates/TAAAA', follow_redirects=True)
        self.assertEqual(b'Ticker not found in dataset', response.data)

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