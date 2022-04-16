import unittest
import inspect

class TestInspectCase(unittest.TestCase):
    def test_case_(self):
        """
        Tests that right price is returned when inputted correct values 
        """
        eqix_open = 227.25;
        output = inspect("EQIX", [2014,12], "Open", "test_data_sample.csv" )
        self.assertEqual(output, equix_open)
        print(output)

if __name__ == '__main__':
    unittest.main()
