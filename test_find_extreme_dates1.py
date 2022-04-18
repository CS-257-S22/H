import sys
import pandas as pd
import unittest
from basic_stock_stat import find_earliest_or_latest_record

class TestInspectCase(unittest.TestCase):
    def test_case_(self):
        """
        Tests that right price is returned when inputted correct values 
        """
        nasdaq_df = pd.read_csv("Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")
        actual = [2010, 1]
        output = find_earliest_or_latest_record("AAPL", "earliest", nasdaq_df)
        self.assertEqual(output, actual)
        print(output)

if __name__ == '__main__':
    unittest.main()
