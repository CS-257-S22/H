import unittest
from basic_stock_stat import basic_stock_stat
from inspect_stock import check_date, check_query, inspect; check_date
from helper import check_ticker

class Tests(unittest.TestCase):

    def testStd_check_ticker(self):
        value = check_ticker("ROST", "Tests/DataForTesting/test_data_sample.csv")
        self.assertEquals(value, True)

    def testWrong_check_ticker(self):
        value = check_ticker("AMOR", "Tests/DataForTesting/test_data_sample.csv")
        self.assertEquals(value, False)

    def test_get_dates(self):

        self.assertEquals()

    def test_inspect(self):

        self.assertEquals()


