import sys
sys.dont_write_bytecode = True

import pandas as pd
import unittest
import sys
sys.path.append('../H/Features')
from inspect_stock import *
from helper import *

nasdaq = get_dataframe()

class TestInspectCaseVolume(unittest.TestCase):
    def test_case_(self):
        """
        Tests that right volume is returned when inputted correct values to find_query function
        """

        output = find_query(6, "AAME", 2016, 5, "Volume", nasdaq)
        actual = 5900.0
        self.assertEqual(float(output), actual)

class TestInspectCaseLow(unittest.TestCase):
    def test_case_(self):
        """
        Tests that right open is returned when inputted correct values to find_query function
        """

        output = find_query(6, "NRCIB", 2015, 8, "Low", nasdaq)
        actual = 32.79999923706055
        self.assertEqual(float(output), actual)

class TestInspectCaseHigh(unittest.TestCase):
    def test_case_(self):
        """
        Tests that right high is returned when inputted correct values to find_query function
        """

        output = find_query(6, "VTNR", 2022, 3, "High", nasdaq)
        actual = 9.44
        self.assertEqual(float(output), actual)

class TestInspectCaseClose(unittest.TestCase):
    def test_case_(self):
        """
        Tests that right close is returned when inputted correct values to find_query function
        """

        output = find_query(6, "PLBC", 2017, 11, "Close", nasdaq)
        actual = 21.39
        self.assertEqual(float(output), actual)

class TestInspectCaseOpen(unittest.TestCase):
    def test_case_(self):
        """
        Tests that right open is returned when inputted correct values to find_query function
        """

        output = find_query(6, "EXPD", 2019, 2, "Open", nasdaq)
        actual = 74.37
        self.assertEqual(float(output), actual)

if __name__ == '__main__':
    unittest.main()