import unittest
import pandas as pd
from basic_stock_stat import get_dates
from helper import check_ticker
from inspect_stock import inspect

class Tests(unittest.TestCase):

    def testStd_check_ticker(self):
        value = check_ticker("ROST", "Tests/DataForTesting/test_data_sample.csv")
        self.assertEquals(value, True)

    def testWrong_check_ticker(self):
        value = check_ticker("AMOR", "Tests/DataForTesting/test_data_sample.csv")
        self.assertEquals(value, False)

    def test_get_dates(self):
        values = get_dates("AMZN", "Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
        trueValues = ([2010, 1], [2022, 3])
        self.assertEquals(values, trueValues)
    
    def testWrong_get_dates(self):
        values = get_dates("AMZN", "Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
        trueValues = ([2009, 2], [2021, 5])
        self.assertEquals(values, trueValues)

    def test_inspect(self):
        nasdaq_df = pd.read_csv("Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
        nasdaq_df["Date"] = pd.to_datetime(nasdaq_df["Date"])

        value = inspect()

        self.assertEquals()


