import unittest
from flask import Flask

import sys
sys.path.append('./Flask')
from Flask_App_main import *

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
    
    def test_route_edge_beginning(self):
        """
        Tests that correct output is returned by the inspect_specified_stock function for first stock in the data set
        """
        self.app = app.test_client()
        response = self.app.get('/inspect_stock/AAL/2010/1/Low', follow_redirects=True)
        self.assertEqual(b"AAL's Low on 1/2010: 5.429999828338623", response.data)
    
    def test_route_edge_end(self):
        """
        Tests that correct output is returned by the inspect_specified_stock function for last stock in the data set
        """
        self.app = app.test_client()
        response = self.app.get('/inspect_stock/ZUMZ/2022/3/Close', follow_redirects=True)
        self.assertEqual(b"ZUMZ's Close on 3/2022: 41.09000015258789", response.data)


if __name__ == '__main__':
    unittest.main()