import unittest

class Tests(unittest.TestCase):

    def test_early_date(self):
        # date = [2010, "June"]
        # consider splitting into two tests if need to reach 16
        date_earliest = basic_stock_stat("AAPL")[0]
        actual_earliest = [2010, 1]
        self.assertEquals(date_earliest, actual_earliest)


    def test_late_date(self):
        date_latest = basic_stock_stat("AAPL")[1]
        actual_latest = [2022, 3]
        self.assertEquals(date_latest, actual_latest)


if __name__ == '__main__':
    unittest.main()

