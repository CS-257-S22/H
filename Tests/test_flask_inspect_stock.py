import unittest
from flask import Flask

import sys
sys.path.append('../Flask')
from Flask_App_Inspect_Stock import *

class TestInspector(unittest.TestCase):
    def test_route_case(self):
        """
        Tests that correct output is returned by the inspect_specified_stock function
        """
        self.app = app.test_client()
        response = self.app.get('/inspect_stock/NLST/2013/11/Volume', follow_redirects=True)
        self.assertEqual(b"NLST's Volume on 11/2013: 376400.0", response.data)
    
    def test_route_bad_ticker(self):
        """
        Tests that correct message is returned by the inspect_specified_stock function to inform the user that their ticker is invalid
        """
        self.app = app.test_client()
        response = self.app.get('/inspect_stock/AKJD/2013/11/Volume', follow_redirects=True)
        self.assertEqual(b"Ticker not found in dataset", response.data)
    
    def test_route_bad_date(self):
        """
        Tests that correct message is returned by the inspect_specified_stock function to inform the user that their date is invalid
        """
        self.app = app.test_client()
        response = self.app.get('/inspect_stock/HBP/2023/11/Open', follow_redirects=True)
        self.assertEqual(b"Invalid Date", response.data)
    
    def test_route_bad_query(self):
        """
        Tests that correct message is returned by the inspect_specified_stock function to inform the user that their input query stat is invalid
        """
        self.app = app.test_client()
        response = self.app.get('/inspect_stock/AAPL/2011/3/Date', follow_redirects=True)
        self.assertEqual(b"Invalid Query", response.data)

if __name__ == '__main__':
    unittest.main()