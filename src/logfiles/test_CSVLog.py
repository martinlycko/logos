# From standard library
import csv
import unittest

# Code to test
from EventLogCSV import EventLogCSV


class TestGoodFiles(unittest.TestCase):

    def test_runningexample(self):
        # Test if the EventLogCSV for runningexample.csv

        runningexample = EventLogCSV(
            filepath="sample_data/running-example.csv",
            delimiter=";",
            time_completed={'Column': 3,
                            'Format': "%d-%m-%Y:%H.%M"},
            id_activity=4,
            id_case=1
        )

        assert runningexample.id_case == 1
        assert runningexample.id_activity == 4
        assert runningexample.time_completed.Column == 3
        assert runningexample.time_completed.Format == "%d-%m-%Y:%H.%M"

        # Test if all optinal collums raise an error when trying to access them
        assert runningexample.id_event is None
        assert runningexample.id_resource is None
        assert runningexample.time_received is None
        assert runningexample.time_ready is None
        assert runningexample.time_start is None
        assert runningexample.time_stop is None
        assert runningexample.attributes_case is None
        assert runningexample.attributes_event is None

        # Set other columns and check their allocation
        runningexample.id_event = 2
        runningexample.id_resource = 5
        runningexample.attributes_event = [6]
        assert runningexample.id_event == 2
        assert runningexample.id_resource == 5
        assert runningexample.attributes_event == [6]
        assert runningexample.attributes_event[0] == 6

        # Double check the allocation matches the content of the event log
        with open(runningexample.filepath) as csv_file:
            csv_reader = csv.reader(csv_file,
                                    delimiter=runningexample.delimiter.value)
            rows = list(csv_reader)
            assert rows[1][runningexample.id_case-1] == "1"
            assert rows[1][runningexample.id_activity-1] == "register request"
            assert rows[1][runningexample.time_completed.Column-1] == "30-12-2010:11.02"
            assert rows[1][runningexample.id_event-1] == "35654423"
            assert rows[1][runningexample.id_resource-1] == "Pete"
            assert rows[1][runningexample.attributes_event[0]-1] == "50"

    def test_flight_event_log(self):
        flightlog = EventLogCSV("sample_data/flight_event_log.csv",
                                ",", 1, 2, 3, "%d/%m/%Y %H:%M")
        assert flightlog.case_original_id.getValue() == 1
        assert flightlog.activity_name.getValue() == 2
        assert flightlog.time_completed.getValue() == 3
        assert flightlog.time_completed.getFormat() == "%d/%m/%Y %H:%M"

    def test_p2p_event_log(self):
        p2pLog = EventLogCSV("sample_data/p2p_event_log.csv",
                             ",", 1, 2, 3, "%Y-%m-%d")
        assert p2pLog.case_original_id.getValue() == 1
        assert p2pLog.activity_name.getValue() == 2
        assert p2pLog.time_completed.getValue() == 3
        assert p2pLog.time_completed.getFormat() == "%Y-%m-%d"

        # Test if all optinal collums raise an error when trying to access
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
