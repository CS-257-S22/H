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
        output = find_query(5, "ACGL", 2014, 9, "Volume", "Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv", nasdaq_df)
        actual = 4090500.0
        self.assertEqual(output, actual)
        print(output)

if __name__ == '__main__':
    unittest.main()