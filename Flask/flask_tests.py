import unittest
from flask_basic_stock_stat import *

class Tests(unittest.TestCase):

    # def test_route(self):
    #     """
    #     This function is a route test for feature 1 of the flask app, which is inspect_stock. It specifies variables 
    #     for the route and checks to see if the function returns the correct output on the page. 
    #     """
    #     self.app = app.test_client()
    #     response = self.app.get('/AMZN/2022/3/Open', follow_redirects=True)
    #     self.assertEqual(b'The Open price for AMZN during month 3 and year 2022 is 2857.0', response.data)

    def test_get_query(self):
        """
        This function is a route test for feature 2 of the flask app, which is basic_stock_stat. It specifies the 
        ticker symbol and checks to see if the function returns the correct dates for the stock on the page. 
        """
        self.app = app.test_client()
        response = self.app.get('/FB', follow_redirects=True)
        self.assertEqual(b'The dates for FB are ([2012, 6], [2022, 3])', response.data)

    def test_get_query_edge_1(self):
        """
        This function is an edge route test for feature 2 of the flask app. It specifies the 
        first ticker symbol of the dataset and checks to see if the function returns the correct 
        dates for the stock on the page.
        """
        self.app = app.test_client()
        response = self.app.get('/AAL', follow_redirects=True)
        self.assertEqual(b'The dates for AAL are ([2010, 1], [2022, 3])', response.data)

    def test_get_query_edge_2(self):
        """
        This function is an edge route test for feature 2 of the flask app. It specifies the 
        last ticker symbol of the dataset and checks to see if the function returns the correct 
        dates for the stock on the page. 
        """
        self.app = app.test_client()
        response = self.app.get('/ZUMZ', follow_redirects=True)
        self.assertEqual(b'The dates for ZUMZ are ([2010, 1], [2022, 3])', response.data)

    def test_get_query_integration(self):
        """
        This function is an integration route test for feature 2 of the flask app. It specifies 
        an incorrect ticker symbol of the dataset and checks to see if the function returns the correct 
        error message for the stock on the page.
        """
        self.app = app.test_client()
        response = self.app.get('/TAAAA', follow_redirects=True)
        self.assertEqual(b'Ticker not in dataset. Please try inputting another ticker symbol instead', response.data)


if __name__ == '__main__':
    unittest.main()
