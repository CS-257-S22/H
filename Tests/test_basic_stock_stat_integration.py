# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

import unittest
import sys
sys.path.append('../H/Features')
from basic_stock_stat import *
import pandas as pd

class TestInspectCase(unittest.TestCase):
    def test_case_(self):
        """
        Integration test that determines if the output of the get_dates function is consistant with the output of
        find_earlist_or_latest_record
        """

        test_dates_sample_df = pd.read_csv("Tests/DataForTesting/test_date_data_sample.csv")

        output_get_dates = get_dates("IIN", 'Tests/DataForTesting/test_date_data_sample.csv')
        output_find_extreme_dates = (find_earliest_or_latest_record("IIN", "earliest",test_dates_sample_df), find_earliest_or_latest_record("IIN", "latest",test_dates_sample_df))
        self.assertEqual(output_get_dates, output_find_extreme_dates)

if __name__ == '__main__':
    unittest.main()