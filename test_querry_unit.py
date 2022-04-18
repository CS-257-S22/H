import pandas as pd
import unittest
from inspect_stock import *
import csv

sample_data = []

with open('Tests/DataForTesting/test_data_sample.csv', mode ='r') as file:
    test_sample_data = csv.reader(file)
    for row in test_sample_data:
        sample_data.append(row)


class TestInspectCase(unittest.TestCase):
    def test_case_(self):
        """
        Tests that right price is returned when inputted correct values

        Uses dummy data in Tests/DataForTesting/test_data_sample.csv to check function
        using 10 dummy stock entries from the main data set.
        """
        nasdaq_df = pd.read_csv("Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv")

        for entry in sample_data[1:]:
            output = find_query(5, str(entry[10]), int(entry[3]), int(entry[2]), "Volume", "Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv", nasdaq_df)
            actual = float(entry[6])
            self.assertEqual(float(output), actual)

if __name__ == '__main__':
    unittest.main()