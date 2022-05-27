# setting path to the directory with the features
import sys
sys.path.append(sys.path[0]+'/../Features')

# UNIVERSAL IMPORT
from universal_import import *

# import other features
import basic_stock_stat
import inspect_stock
import helper
import stock_ROI

class TestInspectCase(unittest.TestCase):
    def test_case_(self):
        """
        Tests that error message is output when an invalid data is input, for the first feature inspect_stock that returns 
        the specified price of a stock from inputted ticker symbol, date, and query. 
        """
        nasdaq_df = helper.get_dataframe()
        
        output = inspect_stock.find_query(6, "AAPL", 2009, 9, "Volume", nasdaq_df)
        error_message = "Invalid Date"
        self.assertEqual(output, error_message)
        print(output)

if __name__ == '__main__':
    unittest.main()
