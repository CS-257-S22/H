import unittest
from inspect_stock import check_date, check_num_args, find_query
import pandas as pd

class Tests(unittest.TestCase):

    def test_find_query(self):
        """
        This is an integration test that tests the find_query method. It uses parameters 
        to substitute for the command line arguments, and uses the dummy dataset for testing
        the function. It is an integration test since it integrates functions that the find_query
        function calls, including inspect() and check_query() among others.
        """
        nasdaq_df = self.get_file()
        self.assertEquals(find_query(5, "GENE", 2017, 11, "Open", "Tests/DataForTesting/test_data_sample.csv", nasdaq_df), 3.200000047683716)

    def test_find_query(self):
        """
        This is an integration test that tests the find_query method. It uses parameters 
        to substitute for the command line arguments, and uses the dummy dataset for testing
        the function. It is an integration test since it integrates functions that the find_query
        function calls, including inspect() and check_query() among others.
        """
        nasdaq_df = self.get_file()
        self.assertEquals(find_query(5, "GENE", 2017, 11, "Open", "Tests/DataForTesting/test_data_sample.csv", nasdaq_df), 3.200000047683716) 

    def test_check_num_args_true(self):
        """
        This is a unit test for the check_num_args function, which is responsible for 
        handling if the number of parameters on the command line is correct. In this test
        it is testing if the function will output True when the number of arguments are the
        right number.
        """
        self.assertTrue(check_num_args(5))

    def test_check_num_args_false(self):
        """
        This is another unit test for the check_num_args function, which is testing
        if the function will output False when the number of arguments are the
        wrong number. 
        """
        self.assertFalse(check_num_args(4))

    def test_check_date_standard(self):
        """
        This is a unit test for the check_date function, which is responsible for 
        handling whether an inputted date for a stock on the command line is valid 
        or not. This unit test checks if the function returns True when inputing a
        date for a stock that is in our dummy dataset.
        """
        self.assertTrue(check_date("AMD", 2017, 3, "Tests/DataForTesting/test_data_sample.csv"))

    def test_check_date_edge(self):
        """
        This is another unit test for the check_date function, and it checks for the edge case
        where the year and the month of the stock is inputted in the wrong order in the command 
        line arguments. This unit test checks if the function returns False when there is an
        inputting error where the year and month parameters are switched on the command line.
        """
        self.assertFalse(check_date("AAA", 3, 2017, "Tests/DataForTesting/test_data_sample.csv"))

    def get_file(self):
        """
        Helper function for accessing the dummy data to avoid multiple layers of abstraction
        Sets the file to the dummy data and returns the dummy data
        """
        nasdaq_df = pd.read_csv("Tests/DataForTesting/test_data_sample.csv")
        nasdaq_df["Date"] = pd.to_datetime(nasdaq_df["Date"])
        return nasdaq_df


if __name__ == '__main__':
    unittest.main()
