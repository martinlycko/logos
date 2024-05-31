# From standard library
import unittest

# To reach to package root folder
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Workaround to make linter happy
if True:
    # Code to test
    from logos.adapters.EventLogCSV import EventLogCSV
    from logos.shared_utils.eventtypes import EventType
    from logos.eventlog.eventlog import EventLog


class MinimalRunningExample(unittest.TestCase):
    # Test analysing the runningexample.csv file with minimal inputs

    def setUp(self) -> None:
        self.sourcefile = EventLogCSV(
            filepath="sample_data/running-example.csv",
            delimiter=";",
            time={'Column': 3,
                  'Format': "%d-%m-%Y:%H.%M",
                  'Stage': EventType.complete},
            id_activity=4,
            id_case=1
        )
        self.eventlog = EventLog()
        self.eventlog.add_events(self.sourcefile)

    def test_activities_add(self) -> None:
        # Tests that 8 activities have been imported
        assert self.eventlog.activities.count() == 8
        # Checks all 8 activities are in the log by name
        assert "register request" in self.eventlog.activities.get_names()
        assert "examine thoroughly" in self.eventlog.activities.get_names()
        assert "check ticket" in self.eventlog.activities.get_names()
        assert "decide" in self.eventlog.activities.get_names()
        assert "reject request" in self.eventlog.activities.get_names()
        assert "examine casually" in self.eventlog.activities.get_names()
        assert "pay compensation" in self.eventlog.activities.get_names()
        assert "reinitiate request" in self.eventlog.activities.get_names()

    def test_cases_add(self) -> None:
        # Tests that 6 cases have been imported
        assert self.eventlog.cases.count() == 6
        # Checks all 8 activities are in the log by name
        assert "1" in self.eventlog.cases.get_names()
        assert "2" in self.eventlog.cases.get_names()
        assert "3" in self.eventlog.cases.get_names()
        assert "4" in self.eventlog.cases.get_names()
        assert "5" in self.eventlog.cases.get_names()
        assert "6" in self.eventlog.cases.get_names()

    def test_resource_add(self) -> None:
        # Tests that no resources have been imported
        assert self.eventlog.resources.count() == 0


class RunningExample(unittest.TestCase):
    # Test analysing the runningexample.csv file with all inputs

    def setUp(self) -> None:
        self.sourcefile = EventLogCSV(
            filepath="sample_data/running-example.csv",
            delimiter=";",
            time={'Column': 3,
                  'Format': "%d-%m-%Y:%H.%M",
                  'Stage': EventType.complete},
            id_activity=4,
            id_case=1,
            id_event=2,
            id_resource=5,
            attributes_event=[6]
        )
        self.eventlog = EventLog()
        self.eventlog.add_events(self.sourcefile)

    def test_activities_add(self) -> None:
        # Tests that 8 activities have been imported
        assert self.eventlog.activities.count() == 8
        # Checks all 8 activities are in the log by name
        assert "register request" in self.eventlog.activities.get_names()
        assert "examine thoroughly" in self.eventlog.activities.get_names()
        assert "check ticket" in self.eventlog.activities.get_names()
        assert "decide" in self.eventlog.activities.get_names()
        assert "reject request" in self.eventlog.activities.get_names()
        assert "examine casually" in self.eventlog.activities.get_names()
        assert "pay compensation" in self.eventlog.activities.get_names()
        assert "reinitiate request" in self.eventlog.activities.get_names()

    def test_cases_add(self) -> None:
        # Tests that 6 cases have been imported
        assert self.eventlog.cases.count() == 6
        # Checks all 8 activities are in the log by name
        assert "1" in self.eventlog.cases.get_names()
        assert "2" in self.eventlog.cases.get_names()
        assert "3" in self.eventlog.cases.get_names()
        assert "4" in self.eventlog.cases.get_names()
        assert "5" in self.eventlog.cases.get_names()
        assert "6" in self.eventlog.cases.get_names()

    def test_resource_add(self) -> None:
        # Tests that 6 resources have been imported
        assert self.eventlog.resources.count() == 6
        # Checks all 6 activities are in the log by name
        assert "Pete" in self.eventlog.resources.get_names()
        assert "Sue" in self.eventlog.resources.get_names()
        assert "Mike" in self.eventlog.resources.get_names()
        assert "Sean" in self.eventlog.resources.get_names()
        assert "Sara" in self.eventlog.resources.get_names()
        assert "Ellen" in self.eventlog.resources.get_names()


if __name__ == "__main__":
    unittest.main()
