# setting path to the directory with the features
import sys
sys.path.append(sys.path[0]+'/../Features')

# UNIVERSAL IMPORT
from universal_import import *

# import other features
import helper
import inspect_stock
import stock_ROI
import basic_stock_stat

class TestInspectCase(unittest.TestCase):
    def test_case_(self):
        """
        Integration test that determines if the output of the get_dates function is consistant with the output of
        find_earlist_or_latest_record
        """

        nasdaq = helper.get_dataframe()

        output_get_dates = basic_stock_stat.get_dates("IIN")
        output_find_extreme_dates = (basic_stock_stat.find_earliest_or_latest_record("IIN", "earliest", nasdaq), basic_stock_stat.find_earliest_or_latest_record("IIN", "latest", nasdaq))
        self.assertEqual(output_get_dates, output_find_extreme_dates)

if __name__ == '__main__':
    unittest.main()

