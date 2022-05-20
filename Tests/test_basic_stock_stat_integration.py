# Pycache are evil, don't produce them
import sys

from Features.helper import get_dataframe
sys.dont_write_bytecode = True

import unittest
import sys
sys.path.append('../H/Features')
from basic_stock_stat import *
from helper import *
import pandas as pd

class TestInspectCase(unittest.TestCase):
    def test_case_(self):
        """
        Integration test that determines if the output of the get_dates function is consistant with the output of
        find_earlist_or_latest_record
        """

        nasdaq = get_dataframe()

        output_get_dates = get_dates("IIN")
        output_find_extreme_dates = (find_earliest_or_latest_record("IIN", "earliest", nasdaq), find_earliest_or_latest_record("IIN", "latest", nasdaq))
        self.assertEqual(output_get_dates, output_find_extreme_dates)

if __name__ == '__main__':
    unittest.main()

