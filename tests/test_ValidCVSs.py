# To reach to package root folder
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Workaround to make linter happy
if True:
    # From standard library
    import csv
    import unittest

    # Code to test
    from logos.adapters.EventLogCSV import EventLogCSV


class MinimalRunningExample(unittest.TestCase):
    # Test if the EventLogCSV for a minimal import of runningexample.csv

    def setUp(self) -> None:
        self.runningexample = EventLogCSV(
            filepath="sample_data/running-example.csv",
            delimiter=";",
            time_completed={'Column': 3,
                            'Format': "%d-%m-%Y:%H.%M",
                            'Stage': "Complete"},
            id_activity=4,
            id_case=1
        )

    def test_attributes(self) -> None:
        # Test if variables are appropriately set
        assert self.runningexample.id_case == 1
        assert self.runningexample.id_activity == 4
        assert self.runningexample.time_completed.Column == 3
        assert self.runningexample.time_completed.Format == "%d-%m-%Y:%H.%M"

        # Test if all optinal columns are not used
        assert self.runningexample.id_event is None
        assert self.runningexample.id_resource is None
        assert self.runningexample.attributes_case is None
        assert self.runningexample.attributes_event is None

    def test_values(self) -> None:
        # Double check the allocation matches the content of the event log
        with open(self.runningexample.filepath) as csv_file:
            csv_reader = csv.reader(csv_file,
                                    delimiter=self.runningexample
                                    .delimiter.value)
            rows = list(csv_reader)
            assert rows[1][self.runningexample
                           .id_case-1] == "1"
            assert rows[1][self.runningexample
                           .id_activity-1] == "register request"
            assert rows[1][self.runningexample
                           .time_completed
                           .Column-1] == "30-12-2010:11.02"


class RunningExample(unittest.TestCase):
    # Test if the EventLogCSV for an import of runningexample.csv

    def setUp(self) -> None:
        self.runningexample = EventLogCSV(
            filepath="sample_data/running-example.csv",
            delimiter=";",
            time_completed={'Column': 3,
                            'Format': "%d-%m-%Y:%H.%M",
                            'Stage': "Complete"},
            id_activity=4,
            id_case=1,
            id_event=2,
            id_resource=5,
            attributes_event=[6]
        )

    def test_attributes(self) -> None:
        # Test if variables are appropriately set
        assert self.runningexample.id_case == 1
        assert self.runningexample.id_activity == 4
        assert self.runningexample.time_completed.Column == 3
        assert self.runningexample.time_completed.Format == "%d-%m-%Y:%H.%M"
        assert self.runningexample.id_event == 2
        assert self.runningexample.id_resource == 5
        assert self.runningexample.attributes_event == [6]

        # Test if all optinal, unused columns are not used
        assert self.runningexample.attributes_case is None

    def test_values(self) -> None:
        # Double check the allocation matches the content of the event log
        with open(self.runningexample.filepath) as csv_file:
            csv_reader = csv.reader(csv_file,
                                    delimiter=self.runningexample
                                    .delimiter.value)
            rows = list(csv_reader)
            assert rows[1][self.runningexample
                           .id_case-1] == "1"
            assert rows[1][self.runningexample
                           .id_activity-1] == "register request"
            assert rows[1][self.runningexample
                           .time_completed
                           .Column-1] == "30-12-2010:11.02"
            assert rows[1][self.runningexample
                           .id_event-1] == "35654423"
            assert rows[1][self.runningexample
                           .id_resource-1] == "Pete"
            assert rows[1][self.runningexample
                           .attributes_event[0]-1] == "50"


class FlightLog(unittest.TestCase):
    # Test if the EventLogCSV for an import of flight_event_log.csv

    def setUp(self) -> None:
        self.flightlog = EventLogCSV(
            filepath="sample_data/flight_event_log.csv",
            delimiter=",",
            time_completed={'Column': 3,
                            'Format': "%d/%m/%Y %H:%M",
                            'Stage': "Complete"},
            id_activity=2,
            id_case=1,
            attributes_event=[4]
        )

    def test_attributes(self) -> None:
        # Test if variables are appropriately set
        assert self.flightlog.id_case == 1
        assert self.flightlog.id_activity == 2
        assert self.flightlog.time_completed.Column == 3
        assert self.flightlog.time_completed.Format == "%d/%m/%Y %H:%M"
        assert self.flightlog.attributes_event == [4]

        # Test if all optinal columns are not used
        assert self.flightlog.id_event is None
        assert self.flightlog.id_resource is None
        assert self.flightlog.attributes_case is None

    def test_values(self) -> None:
        # Double check the allocation matches the content of the event log
        with open(self.flightlog.filepath) as csv_file:
            csv_reader = csv.reader(csv_file,
                                    delimiter=self.flightlog
                                    .delimiter.value)
            rows = list(csv_reader)
            assert rows[1][self.flightlog
                           .id_case-1] == "TR320"
            assert rows[1][self.flightlog
                           .id_activity-1] == "Check-in"
            assert rows[1][self.flightlog
                           .time_completed
                           .Column-1] == "01/12/2019 12:01"
            assert rows[1][self.flightlog
                           .attributes_event[0]-1] == "Munich"


class P2PLog(unittest.TestCase):
    # Test if the EventLogCSV for an import of p2p_event_log.csv

    def setUp(self) -> None:
        self.p2plog = EventLogCSV(
            filepath="sample_data/p2p_event_log.csv",
            delimiter=",",
            time_completed={'Column': 3,
                            'Format': "%Y-%m-%d",
                            'Stage': "Complete"},
            id_activity=2,
            id_case=1,
        )

    def test_attributes(self) -> None:
        # Test if variables are appropriately set
        assert self.p2plog.id_case == 1
        assert self.p2plog.id_activity == 2
        assert self.p2plog.time_completed.Column == 3
        assert self.p2plog.time_completed.Format == "%Y-%m-%d"

        # Test if all optinal columns are not used
        assert self.p2plog.id_event is None
        assert self.p2plog.id_resource is None
        assert self.p2plog.attributes_case is None
        assert self.p2plog.attributes_event is None

    def test_values(self) -> None:
        # Double check the allocation matches the content of the event log
        with open(self.p2plog.filepath) as csv_file:
            csv_reader = csv.reader(csv_file,
                                    delimiter=self.p2plog
                                    .delimiter.value)
            rows = list(csv_reader)
            assert rows[1][self.p2plog
                           .id_case-1] == "1116492"
            assert rows[1][self.p2plog
                           .id_activity-1] == "Scan Invoice"
            assert rows[1][self.p2plog
                           .time_completed
                           .Column-1] == "2016-02-07"


if __name__ == "__main__":
    unittest.main()
