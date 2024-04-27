import csv

import unittest
from EventLogCSV import EventLogCSV

class TestGoodFiles(unittest.TestCase):
    
    def test_runningexample(self):
        # Test if constructor rsets the correct values for running-example.csv
        csvlog = EventLogCSV("sample_data/running-example.csv", ";", 1, 4, 3,"%d-%m-%Y:%H.%M")
        assert csvlog.case_original_id.getValue() == 1
        assert csvlog.activity_name.getValue() == 4
        assert csvlog.time_completed.getValue() == 3
        assert csvlog.time_completed.getFormat() == "%d-%m-%Y:%H.%M"

        # Test if all optinal collums raise an error when trying to access them
        with self.assertRaises(ValueError):
            csvlog.event_original_id.getValue()
        with self.assertRaises(ValueError):
            csvlog.time_received.getValue()
        with self.assertRaises(ValueError):
            csvlog.time_ready.getValue()
        with self.assertRaises(ValueError):
            csvlog.time_start.getValue()
        with self.assertRaises(ValueError):
            csvlog.time_stop.getValue()
        with self.assertRaises(ValueError):
            csvlog.resource_name.getValue()
        with self.assertRaises(ValueError):
            csvlog.case_attributes.getValue()
        with self.assertRaises(ValueError):
            csvlog.event_attributes.getValue()
 
        # Set other columns and check their allocation
        csvlog.set_EventID_Column(2)
        csvlog.set_ResourceName_Column(5)
        csvlog.set_EventAttributes_Column(6)
        assert csvlog.event_original_id.getValue() == 2
        assert csvlog.resource_name.getValue() == 5
        assert csvlog.event_attributes.getValue() == 6

        # Double check the allocation matches the content of the event log
        with open(csvlog.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=csvlog.delimiter)
            rows = list(csv_reader)
            assert rows[1][csvlog.case_original_id.getValue()-1] == "1"
            assert rows[1][csvlog.activity_name.getValue()-1] == "register request"
            assert rows[1][csvlog.time_completed.getValue()-1] == "30-12-2010:11.02"
            assert rows[1][csvlog.event_original_id.getValue()-1] == "35654423"
            assert rows[1][csvlog.resource_name.getValue()-1] == "Pete"
            assert rows[1][csvlog.event_attributes.getValue()-1] == "50"

    def test_flight_event_log(self):
        pass
        # flightlog = EventLogCSV("sample_data/flight_event_log.csv", ",", 1, 2, 3, "%d/%m/%Y %H:%M")

    def p2p_event_log(self):
        p2pLog = EventLogCSV("sample_data/p2p_event_log.csv", ",", 1, 2, 3, "%Y-%m-%d")
        assert p2pLog.case_original_id.getValue() == 1
        assert p2pLog.activity_name.getValue() == 2
        assert p2pLog.time_completed.getValue() == 3
        assert p2pLog.time_completed.getFormat() == "%Y-%m-%d"

         # Test if all optinal collums raise an error when trying to access them
        with self.assertRaises(ValueError):
            p2pLog.event_original_id.getValue()
        with self.assertRaises(ValueError):
            p2pLog.time_received.getValue()
        with self.assertRaises(ValueError):
            p2pLog.time_ready.getValue()
        with self.assertRaises(ValueError):
            p2pLog.time_start.getValue()
        with self.assertRaises(ValueError):
            p2pLog.time_stop.getValue()
        with self.assertRaises(ValueError):
            p2pLog.resource_name.getValue()
        with self.assertRaises(ValueError):
            p2pLog.case_attributes.getValue()
        with self.assertRaises(ValueError):
            p2pLog.event_attributes.getValue()

        # Double check the allocation matches the content of the event log
        with open(p2pLog.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=p2pLog.delimiter)
            rows = list(csv_reader)
            assert rows[1][p2pLog.case_original_id.getValue()-1] == "1116492"
            assert rows[1][p2pLog.activity_name.getValue()-1] == "Scan Invoice"
            assert rows[1][p2pLog.time_completed.getValue()-1] == "2016-02-07"

if __name__ == "__main__":
    unittest.main()