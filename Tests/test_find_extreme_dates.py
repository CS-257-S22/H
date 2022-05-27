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
        Tests that right data is return for a specific valid ticker
        """
        nasdaq_df = pd.read_csv("Data/Polished/randomized_day_market.csv")
        actual = [2012, 1, 18]
        output = basic_stock_stat.find_earliest_or_latest_record("AAPL", "earliest", nasdaq_df)
        self.assertEqual(output, actual)
        print(output)

if __name__ == '__main__':
    unittest.main()
