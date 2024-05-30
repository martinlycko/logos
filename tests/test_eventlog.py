# From standard library
import csv
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
    # Test if the EventLogCSV for a minimal import of runningexample.csv

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

    def test_activities(self) -> None:
        # Test all activities have been imported
        assert self.eventlog.activities.count() == 8
        # Check all 8 activities are in the log
        assert "register request" in self.eventlog.activities.get_names()
        assert "examine thoroughly" in self.eventlog.activities.get_names()
        assert "check ticket" in self.eventlog.activities.get_names()
        assert "decide" in self.eventlog.activities.get_names()
        assert "reject request" in self.eventlog.activities.get_names()
        assert "examine casually" in self.eventlog.activities.get_names()
        assert "pay compensation" in self.eventlog.activities.get_names()
        assert "reinitiate request" in self.eventlog.activities.get_names()


if __name__ == "__main__":
    unittest.main()
