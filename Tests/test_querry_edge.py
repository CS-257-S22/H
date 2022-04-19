import sys
sys.path.append('../H')
import pandas as pd
import unittest
from inspect_stock import *

class TestInspectCase(unittest.TestCase):
    def test_case_(self):
        """
        Tests that error message is output when an invalid  data is input 
        """
        nasdaq_df = pd.read_csv("Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
        output = find_query(5, "AAPL", 2009, 9, "Volume", "Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv", nasdaq_df)
        error_message = "Invalid Date"
        self.assertEqual(output, error_message)
        print(output)

if __name__ == '__main__':
    unittest.main()