import sys
import pandas as pd
import unittest
from inspect_stock import *

class TestInspectCase(unittest.TestCase):
    def test_case_(self):
        """
        Tests that right price is returned when inputted correct values 
        """
        nasdaq_df = pd.read_csv("Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
        output = find_earliest_or_latest_record("A", "earliest", nasdaq_df)
        print(type(output[0]))
        self.assertTrue()
        print(output)

if __name__ == '__main__':
    unittest.main()