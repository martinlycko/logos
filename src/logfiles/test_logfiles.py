import unittest
from EventLogCSV import EventLogCSV

class TestCSVFilepaths(unittest.TestCase):

    def test_emptyfilepath(self):
        # Test if constructor raises an exception for empty filepath
        with self.assertRaises(FileNotFoundError):
            csvlog = EventLogCSV("", ";", 1, 2, 3,"%d-%m-%Y:%H.%M")

    def test_nofileatpath(self):
        # Test if constructor raises an exception when file does not exist at provided path
        with self.assertRaises(FileNotFoundError):
            csvlog = EventLogCSV("sample_data/nofile.csv", ";", 1, 2, 3,"%d-%m-%Y:%H.%M")

    def test_XESfile(self):
        # Test if constructor raises an exception when file is not a CSV
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.xes",  ";", 1, 2, 3,"%d-%m-%Y:%H.%M")

    def test_TXTfile(self):
        # Test if constructor raises an exception when file is not a CSV
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.txt",  ";", 1, 2, 3,"%d-%m-%Y:%H.%M")

class TestCSVEventIDColumn(unittest.TestCase):
    
    def test_ColumnNumTooHigh(self):
        # Test if constructor raises an exception for empty filepath
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv",  ";", 7, 2, 3,"%d-%m-%Y:%H.%M")

if __name__ == "__main__":
    unittest.main()

    # Tests to create:
    # Column number does not exist in file
    # Column includes empty values