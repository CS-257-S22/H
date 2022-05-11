# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

import sys
sys.path.append('../H/Features')
import pandas as pd
import unittest
from basic_stock_stat import find_earliest_or_latest_record

class TestInspectCase(unittest.TestCase):
    def test_case_(self):
        """
        Tests that right data is return for a specific valid ticker
        """
        nasdaq_df = pd.read_csv("Data/Polished/randomized_day_market.csv")
        actual = [2012, 1]
        output = find_earliest_or_latest_record("AAPL", "earliest", nasdaq_df)
        self.assertEqual(output, actual)
        print(output)

if __name__ == '__main__':
    unittest.main()
