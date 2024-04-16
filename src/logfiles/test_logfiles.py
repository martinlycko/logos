import csv

import unittest
from EventLogCSV import EventLogCSV

class TestCSVFile(unittest.TestCase):

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
            csvlog = EventLogCSV("sample_data/running-example.xes", ";", 1, 2, 3,"%d-%m-%Y:%H.%M")

    def test_TXTfile(self):
        # Test if constructor raises an exception when file is not a CSV
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.txt", ";", 1, 2, 3,"%d-%m-%Y:%H.%M")

    def test_WrongDelimiter(self):
        # Test if constructor raises an exception when an incorrect delimiter is provided
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.txt", ",", 1, 2, 3,"%d-%m-%Y:%H.%M")

class TestCSVCaseIDColumn(unittest.TestCase):
    
    def test_ColumnNumTooHigh(self):
        # Test if constructor raises an exception if the column number is too high
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 7, 4, 3,"%d-%m-%Y:%H.%M")

    def test_EmptyField(self):
        # Test if the constructor raises an exception if the EventID contains empty values
         with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example - missing CaseID.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")

class TestCSVActivityNameColumn(unittest.TestCase):
    
    def test_ColumnNumTooHigh(self):
        # Test if constructor raises an exception if the column number is too high
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 7, 3,"%d-%m-%Y:%H.%M")

    def test_EmptyField(self):
        # Test if the constructor raises an exception if the EventID contains empty values
         with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example - missing Activity.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")

class TestCSVCompletionTimeColumn(unittest.TestCase):
    
    def test_ColumnNumTooHigh(self):
        # Test if constructor raises an exception if the column number is too high
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 7,"%d-%m-%Y:%H.%M")

    def test_EmptyField(self):
        # Test if the constructor raises an exception if the EventID contains empty values
         with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example - missing Timestamp.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")

    def test_DifferentFormatProvided(self):
        # Test if constructor raises an exception for empty filepath
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y-%H.%M")

    def test_InconsitentFormat(self):
        # Test if the constructor raises an exception if the EventID contains empty values
         with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example - different Timestamp.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")

class TestGoodFiles(unittest.TestCase):
    
    def test_runningexample(self):
        # Test if constructor rsets the correct values for running-example.csv
        csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
        assert csvlog.case_original_id.getValue() == 1
        assert csvlog.activity_name.getValue() == 4
        assert csvlog.time_completed.getValue() == 3
        assert csvlog.time_completed.getFormat() == "%d-%m-%Y:%H.%M"

        # Double check the allocation matches the content of the event log
        with open(csvlog.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=csvlog.delimiter)
            rows = list(csv_reader)
            assert rows[1][csvlog.case_original_id.getValue()-1] == "1"
            assert rows[1][csvlog.activity_name.getValue()-1] == "register request"
            assert rows[1][csvlog.time_completed.getValue()-1] == "30-12-2010:11.02"

if __name__ == "__main__":
    unittest.main()