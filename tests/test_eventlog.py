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

    def test_events_add(self) -> None:
        # Tests that 42 events have been imported
        assert self.eventlog.events.count() == 42
        # Check that names have not been imported
        assert self.eventlog.events.eventList[0].name is None
        assert self.eventlog.events.eventList[41].name is None

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

    def test_events_add(self) -> None:
        # Tests that 42 events have been imported
        assert self.eventlog.events.count() == 42
        # Check some of the names have been imported
        assert "35654423" in self.eventlog.events.get_names()
        assert "35654718" in self.eventlog.events.get_names()
        assert "35654877" in self.eventlog.events.get_names()

    def test_events_enrich(self) -> None:
        # Checks that events for cases have been set correctly
        self.event35654423ID = self.eventlog.events.get_id("35654423")
        self.event = self.eventlog.events.eventList[self.event35654423ID]
        # Check that case has been set correctly
        assert self.event.case.name == "1"
        # check that activities has been set correctly
        assert self.event.activity.name == "register request"
        # Check that resource has been set correctly
        assert self.event.resource.name == "Pete"

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

    def test_activities_enrich(self) -> None:
        # Checks that events for resources have been set correctly
        self.activityDecideID = self.eventlog.activities.get_id("decide")
        self.activityDecide = self.eventlog.activities.activityList[self.activityDecideID]
        self.activityRegisterID = self.eventlog.activities.get_id("register request")
        self.activityRegister = self.eventlog.activities.activityList[self.activityRegisterID]
        assert self.activityDecide.count_events() == 9
        assert self.activityRegister.count_events() == 6
        assert self.activityDecide.events[0].name == "35654488"
        assert self.activityRegister.events[0].name == "35654423"
        # Checks that cases have been set correctly
        assert self.activityDecide.count_cases() == 6
        assert self.activityRegister.count_cases() == 6
        # Checks that resources have been set correctly
        assert self.activityDecide.count_resources() == 1
        assert self.activityRegister.count_resources() == 3

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

    def test_cases_enrich(self) -> None:
        # Checks that events for cases have been set correctly
        self.case1ID = self.eventlog.cases.get_id("1")
        self.case1 = self.eventlog.cases.caseList[self.case1ID]
        self.case3ID = self.eventlog.cases.get_id("3")
        self.case3 = self.eventlog.cases.caseList[self.case3ID]
        assert self.case1.count_events() == 5
        assert self.case3.count_events() == 9
        assert self.case1.events[0].name == "35654423"
        assert self.case3.events[0].name == "35654521"
        # Checks that activities have been set correctly
        assert self.case1.count_activities() == 5
        assert self.case3.count_activities() == 7
        # Checks that resources have been set correctly
        assert self.case1.count_resources() == 4
        assert self.case3.count_resources() == 5

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

    def test_resource_enrich(self) -> None:
        # Checks that events for resources have been set correctly
        self.resourcePeteID = self.eventlog.resources.get_id("Pete")
        self.resourcePete = self.eventlog.resources.resourceList[self.resourcePeteID]
        self.resourceSaraID = self.eventlog.resources.get_id("Sara")
        self.resourceSara = self.eventlog.resources.resourceList[self.resourceSaraID]
        assert len(self.resourcePete.events) == 7
        assert len(self.resourceSara.events) == 12
        # Checks that activities have been set correctly
        assert len(self.resourcePete.activities) == 3
        assert len(self.resourceSara.activities) == 2
        # Checks that cases have been set correctly
        assert len(self.resourcePete.cases) == 4
        assert len(self.resourceSara.cases) == 6


if __name__ == "__main__":
    unittest.main()
