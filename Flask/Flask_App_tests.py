import unittest
from Flask_App_main import *

class Tests(unittest.TestCase):

    def test_get_query(self):
        """
        This function is a route test for feature 2 of the flask app, which is basic_stock_stat. It specifies the 
        ticker symbol and checks to see if the function returns the correct dates for the stock on the page. 
        """
        self.app = app.test_client()
        response = self.app.get('/extreme_dates/FB', follow_redirects=True)
        self.assertEqual(b'The dates for FB are ([2012, 6], [2022, 3])', response.data)

    def test_get_query_edge_1(self):
        """
        This function is an edge route test for feature 2 of the flask app. It specifies the 
        first ticker symbol of the dataset and checks to see if the function returns the correct 
        dates for the stock on the page.
        """
        self.app = app.test_client()
        response = self.app.get('/extreme_dates/AAL', follow_redirects=True)
        self.assertEqual(b'The dates for AAL are ([2010, 1], [2022, 3])', response.data)

    def test_get_query_edge_2(self):
        """
        This function is an edge route test for feature 2 of the flask app. It specifies the 
        last ticker symbol of the dataset and checks to see if the function returns the correct 
        dates for the stock on the page. 
        """
        self.app = app.test_client()
        response = self.app.get('/extreme_dates/ZUMZ', follow_redirects=True)
        self.assertEqual(b'The dates for ZUMZ are ([2010, 1], [2022, 3])', response.data)

    def test_get_query_integration(self):
        """
        This function is an integration route test for feature 2 of the flask app. It specifies 
        an incorrect ticker symbol of the dataset and checks to see if the function returns the correct 
        error message for the stock on the page.
        """
        self.app = app.test_client()
        response = self.app.get('/extreme_dates/TAAAA', follow_redirects=True)
        string = self.display_error_message()
        self.assertEqual(bytes(string, encoding='utf-8'), response.data)

    def display_error_message(self):
        """
        """
        # the message to be displayed
        message404 = "ERROR 404\n\nInvalid route.\nReturn to Home Page for more instruction. (i.e. You can use the Back button.)"

        # convert the message to html-friendly format
        message404 = message404.replace('\n', '<br>')

        return message404


if __name__ == '__main__':
    unittest.main()
