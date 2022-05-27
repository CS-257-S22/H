# setting path to the directory with the features
import sys
sys.path.append(sys.path[0]+'/../Features')

# UNIVERSAL IMPORT
from universal_import import *

# import other features
import basic_stock_stat
import inspect_stock
import helper
import stock_ROI

class Tests(unittest.TestCase):

    def test_check_ticker(self):
        """Tests whether the check_ticker method properly recognizes that a ticker is in the dataset"""
        value = helper.check_ticker("ROST")
        self.assertEqual(value, True)

    def test_wrong_check_ticker(self):
        """Tests wheter the check_tciker method properly recognizes that a ticker is NOT in the dataset"""
        value = helper.check_ticker("AMOR")
        self.assertEqual(value, False)

    def test_get_dates(self):
        """Tests whether or not the correct dates are retreived when calling the get_dates method"""
        values = basic_stock_stat.get_dates("AMZN")
        trueValues = ([2012, 1, 23], [2022, 4, 4])
        self.assertEqual(values, trueValues)
    
    def test_wrong_get_dates(self):
        """Tests whether or not an incorrect date value is recognized as being so"""
        values = basic_stock_stat.get_dates("AMZN")
        trueValues = ([2009,2], [2021,5])
        self.assertFalse(values == trueValues)

    def test_inspect(self):
        """Test whether the correct value is retreieved when calling the method inspect, which itself relies
        on the integration of several other methods"""
        testData = pd.read_csv("Tests/DataForTesting/test_data_sample.csv")
        # testData = pd.read_csv("Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
        testData["Date"] = pd.to_datetime(testData["Date"])

        value = inspect_stock.inspect("ROST", [2020, 10], "Low", testData)
        trueValue = 94.87999725
        self.assertEqual(value, trueValue)
    
    def test_wrong_inspect(self):
        """This tests if when an incorrect value is inputted whether it is recognized as being incorrect or not"""
        testData = pd.read_csv("Tests/DataForTesting/test_data_sample.csv")
        # testData = pd.read_csv("Data/Polished/randomized_day_market.csv")
        testData["Date"] = pd.to_datetime(testData["Date"])

        value = inspect_stock.inspect("ROST", [2020, 10], "Low", testData)
        trueValue = 95

        self.assertFalse(value == trueValue)


if __name__ == '__main__':
    unittest.main()
