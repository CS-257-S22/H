import unittest
from basic_stock_stat import basic_stock_stat
from inspect_stock import check_query; check_date

class Tests(unittest.TestCase):

    def test_early_date(self):
        # consider splitting into two tests if need to reach 16
        date_earliest = basic_stock_stat("AAPL")[0]
        # added a for loop and list to loop through 10 stocks
        stocks_earliest_dates = []
        for i in range(0, len(stocks_earliest_dates)):
            self.assertEquals(date_earliest, stocks_earliest_dates[i])

        # actual_earliest = [2010, 1]


    def test_late_date(self):
        date_latest = basic_stock_stats("AAPL")[1]
        actual_latest = [2022, 3]
        self.assertEquals(date_latest, actual_latest)

    def test_check_query(self):
        
        self.assertEquals(check_query("High"), True)
        self.assertEquals(check_query("AdjustedLow"), False)

    def test_check_date(self):

        self.assertEquals()

    
    


if __name__ == '__main__':
    unittest.main()
