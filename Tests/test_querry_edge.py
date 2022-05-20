# Pycache are evil, don't produce them
import sys
sys.dont_write_bytecode = True

import sys
sys.path.append('../H/Features')
import pandas as pd
import unittest
from inspect_stock import *
from helper import *

class TestInspectCase(unittest.TestCase):
    def test_case_(self):
        """
        Tests that error message is output when an invalid data is input, for the first feature inspect_stock that returns 
        the specified price of a stock from inputted ticker symbol, date, and query. 
        """
        nasdaq_df = get_dataframe()
        
        output = find_query(6, "AAPL", 2009, 9, "Volume", nasdaq_df)
        error_message = "Invalid Date"
        self.assertEqual(output, error_message)
        print(output)

if __name__ == '__main__':
    unittest.main()
