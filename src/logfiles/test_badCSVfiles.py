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

class TestCaseIDColumn(unittest.TestCase):
    
    def test_ColumnNumTooHigh(self):
        # Test if constructor raises an exception if the column number is too high
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 7, 4, 3,"%d-%m-%Y:%H.%M")

    def test_EmptyField(self):
        # Test if the constructor raises an exception if the EventID contains empty values
         with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example - missing CaseID.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")

    def test_duplicatecolumnusage(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 1, 3,"%d-%m-%Y:%H.%M")

    def test_nonIntegerColumn(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", "1", 1, 3,"%d-%m-%Y:%H.%M")

    def test_nonNegativeColumn(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", -1, 1, 3,"%d-%m-%Y:%H.%M")

class TestActivityNameColumn(unittest.TestCase):
    
    def test_ColumnNumTooHigh(self):
        # Test if constructor raises an exception if the column number is too high
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 7, 3,"%d-%m-%Y:%H.%M")

    def test_EmptyField(self):
        # Test if the constructor raises an exception if the EventID contains empty values
         with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example - missing Activity.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")

    def test_DuplicateColumnUse(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 1, 3,"%d-%m-%Y:%H.%M")

    def test_nonIntegerColumn(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, "1", 3,"%d-%m-%Y:%H.%M")

    def test_nonNegativeColumn(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, -1, 3,"%d-%m-%Y:%H.%M")

class TestTimeCompletionColumn(unittest.TestCase):
    
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

    def test_DuplicateColumnUse(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 4,"%d-%m-%Y:%H.%M")

    def test_nonIntegerColumn(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 1, "3","%d-%m-%Y:%H.%M")

    def test_nonNegativeColumn(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 1, -3,"%d-%m-%Y:%H.%M")

class TestEventIDColumn(unittest.TestCase):

    def test_ColumnNumTooHigh(self):
        # Test if constructor raises an exception if the column number is too high
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_EventID_Column(7)

    def test_EmptyField(self):
        # Test if the constructor raises an exception if the EventID contains empty values
         with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example - missing EventID.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_EventID_Column(2)

    def test_DuplicateColumnUse(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_EventID_Column(1)

    def test_nonIntegerColumn(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_EventID_Column("2")

    def test_nonNegativeColumn(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_EventID_Column(-2)

# class TestTimeReceivedColumn(unittest.TestCase):

# class TestTimeReadyColumn(unittest.TestCase):

# class TestTimeStartColumn(unittest.TestCase):

# class TestTimeStopColumn(unittest.TestCase):

class TestResourceNameColumn(unittest.TestCase):
    
    def test_ColumnNumTooHigh(self):
        # Test if constructor raises an exception if the column number is too high
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_ResourceName_Column(7)

    def test_DuplicateColumnUse(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_ResourceName_Column(1)

    def test_nonIntegerColumn(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_ResourceName_Column("5")

    def test_nonNegativeColumn(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_ResourceName_Column(-5)

class TestCaseAttributeColumns(unittest.TestCase):
    
    def test_ScalarColumnNumTooHigh(self):
        # Test if constructor raises an exception if the column number is too high
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_CaseAttributes_Column(7)

    def test_ListColumnNumTooHigh(self):
        # Test if constructor raises an exception if the column number is too high
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_CaseAttributes_Column([2, 7])

    def test_DuplicateColumnUse(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_CaseAttributes_Column(1)

    def test_nonIntegerColumn(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_CaseAttributes_Column("2")

    def test_nonNegativeColumn(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_CaseAttributes_Column(2)

    def test_DuplicateColumnsUsage(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_CaseAttributes_Column([1, 6])

    def test_nonIntegerColumns(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_CaseAttributes_Column(["1", 6])

    def test_nonNegativeColumns(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_CaseAttributes_Column([-1, 6])

class TestEventAttributeColumns(unittest.TestCase):
    
    def test_ScalarColumnNumTooHigh(self):
        # Test if constructor raises an exception if the column number is too high
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_EventAttributes_Column(7)

    def test_ListColumnNumTooHigh(self):
        # Test if constructor raises an exception if the column number is too high
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_EventAttributes_Column([2, 7])

    def test_DuplicateColumnUse(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_EventAttributes_Column(1)

    def test_nonIntegerColumn(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_EventAttributes_Column("2")

    def test_nonNegativeColumn(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_EventAttributes_Column(2)

    def test_DuplicateColumnsUsage(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_EventAttributes_Column([1, 6])

    def test_nonIntegerColumns(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_EventAttributes_Column(["1", 6])

    def test_nonNegativeColumns(self):
        with self.assertRaises(ValueError):
            csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
            csvlog.set_EventAttributes_Column([-1, 6])

if __name__ == "__main__":
    unittest.main()