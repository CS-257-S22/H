# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

import unittest

import argparse
import pandas as pd

import path
# current directory
directory = path.Path(__file__).abspath()
# setting path to the directory with the feature
sys.path.append(directory.parent.parent)
sys.path.append("Features")

# importing the functions we are testing
from stock_ROI import *
from inspect_stock import check_query

# specifying path to test data
data_file = "Tests/DataForTesting/test_data_fabricated.csv"

class test_stock_ROI(unittest.TestCase):

    def test_main_stock_ROI(self):
        """
        INTEGRATION TEST for main_stock_ROI()
            1. This method test the integration of the main_stock_ROI() method with all of its helper functions to produce\
                the appropriate result
        """

        # list of inputs
        given = [["AMD", [2017, 3] , [2021, 7], "Low", "High"],\
            ["RIBT", [2015, 3], [2021, 3], "Open", "High"],\
            ["GENE", [2017, 11], [2021, 6], "Open", "High"],\
            ["SAFM", [2017, 9], [2021, 3], "High", "Low"]]

        # list of corresponding expected output
        expected = [555.604,\
            -78.788,\
            19.277,\
            -1.647]
        
        # loop through the list of given and expected outcome and compare multiple cases
        for i in range(len(given)):
            self.assertAlmostEqual(round(float(main_stock_ROI(\
                given[i][0], given[i][1], given[i][2], given[i][3], given[i][4], data_file)), ndigits = 3),\
                expected[i], places = 3)

    #------------------------------

    def test_all_input_is_valid_stock_ROI(self):
        """
        UNIT TEST for method all_input_is_valid_stock_ROI()
        """

        # read in dummy data
        dummy_df = pd.read_csv(data_file)

        # list of inputs
        given = [["AMD", [2017, 3] , [2030, 7], "Low", "High"],\
            ["RIBT", [2010, 3], [2030, 3], "Open", "High"],\
            ["GEne", [2017, 11], [2030, 6], "Open", "Close"],\
            ["HWBK", [2099, 2], [2030, 8], "Adjusted Close", "Open"],\
            ["SAFM", [2017, 9], [2030, 3], "Baka", "Low"]]

        # list of corresponding expected output
        expected = [True, True,\
            "INPUT ERROR: Invalid ticker symbol. Please choose one that exists within our data instead.",\
            "INPUT ERROR: Invalid year for investment date.",\
            "INPUT ERROR: Invalid buying price. Choose between 'Open', 'Close', 'High', 'Close', and 'Adjusted Close' only."]

        # loop through the list of given and expected outcome and compare multiple cases
        for i in range(len(given)):
            self.assertEqual(all_input_is_valid_stock_ROI(dummy_df,\
                given[i][0], given[i][1], given[i][2], given[i][3], given[i][4]),\
                expected[i])

    #------------------------------

    def test_in_dataframe(self):
        """
        UNIT TEST for method in_data_frame()
        """

        # read in dummy data
        dummy_df = pd.read_csv(data_file)

        # list of inputs
        given = [[1434200, "Volume"],\
            ["sfbhvsg", "Ticker Symbol"],\
            [15, "Day"],\
            [999, "Open"]]

        # list of corresponding expected output
        expected = [True,\
            False,\
            True,\
            False]

        # loop through the list of given and expected outcome and compare multiple cases
        for i in range(len(given)):
            self.assertEqual(in_dateframe(given[i][0], given[i][1], dummy_df),\
            expected[i])

    #------------------------------

    def test_backbone_stock_ROI(self):
        """
        UNIT TEST for method test_backbone_stock_ROI()
        """

        # read in dummy data
        dummy_df = pd.read_csv(data_file)

        # list of inputs
        given = [["AMD", [2017, 3] , [2030, 7], "Low", "High"],\
            ["RIBT", [2010, 3], [2030, 3], "Open", "High"],\
            ["GENE", [2017, 11], [2030, 6], "Open", "Close"],\
            ["SAFM", [2017, 9], [2030, 3], "Close", "Low"]]

        # list of corresponding expected output
        expected = [5292.308,\
            1577.778,\
            1133.333,\
            -92.2581]
        
        # loop through the list of given and expected outcome and compare multiple cases
        for i in range(len(given)):
            self.assertAlmostEqual(round(backbone_stock_ROI(dummy_df,\
                given[i][0], given[i][1], given[i][2], given[i][3], given[i][4]), ndigits=3),\
                expected[i], places = 3)

    #------------------------------

    def test_percentage_difference(self):
        """
        UNIT TEST for method percentage_difference()
        """

        # list of input
        given = [[30, 5], [145.416, 466156], [-145, 415]]

        # list of corresponding expected output
        expected = [-83.333, 320467.200, -386.207]

        for i in range(len(given)):
            self.assertAlmostEqual(round(percentage_difference(given[i][0], given[i][1]), ndigits = 3), \
            expected[i], places = 3)


if __name__ == '__main__':
    unittest.main()