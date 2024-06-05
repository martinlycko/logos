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
    from logos.eventlog.analysis.paths import Paths
    from logos.eventlog.analysis.path import Path


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
        self.eventlog.analyse_paths()

    def test_case_paths(self) -> None:
        self.case1 = self.eventlog.cases.get("1")
        len(self.case1.path) == 5
        self.case1.path[0].name == "register request"
        self.case1.path[1].name == "examine thoroughly"
        self.case1.path[2].name == "check ticket"
        self.case1.path[3].name == "decide"
        self.case1.path[4].name == "reject request"

    def test_paths(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
