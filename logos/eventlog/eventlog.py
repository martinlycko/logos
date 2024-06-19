# For type safety and code quality
from pydantic import BaseModel

# From standard library
import csv
from datetime import datetime

# Reference to other event log classes
from logos.eventlog.elements.activities import Activities
from logos.eventlog.elements.cases import Cases
from logos.eventlog.elements.resources import Resources
from logos.eventlog.elements.events import Events
from logos.eventlog.analysis.pathing.paths.paths import Paths
from logos.eventlog.analysis.pathing.pathtree.pathtree import PathTree

# Import of supported adapter classes for source logs
from logos.adapters.EventLogCSV import EventLogCSV


class EventLog(BaseModel):
    # A class to capture the entire event log structure
    events: Events = Events()               # Contains a list of all events
    activities: Activities = Activities()   # Contains a list of all activities
    cases: Cases = Cases()                  # Contains a list of all cases
    resources: Resources = Resources()      # Contains a list of all resources
    paths: Paths = Paths()                  # Contains a list of paths
    pathtree: PathTree = PathTree()

    def add_events(self, sourcelog) -> None:
        # Imports event logs parsed through the adapter classes

        if isinstance(sourcelog, EventLogCSV):
            # Open the CSV file with its specified path
            with open(sourcelog.filepath) as csv_file:
                csv_reader = csv.reader(csv_file,
                                        delimiter=sourcelog.delimiter.value)
                line_count = 1
                for row in csv_reader:
                    # Ignore the first row commonly including headers
                    if line_count == 1:
                        pass
                    else:
                        # Collect all mandatory columns from the event log
                        activityName = row[sourcelog.id_activity-1]
                        caseName = row[sourcelog.id_case-1]
                        time = datetime.strptime(row[sourcelog.time.Column-1],
                                                 sourcelog.time.Format)
                        stage = sourcelog.time.Stage

                        # Collect all optional columns from the event log
                        if sourcelog.id_resource is None:
                            resourceName = None
                        else:
                            resourceName = row[sourcelog.id_resource-1]

                        if sourcelog.id_event is None:
                            eventName = None
                        else:
                            eventName = row[sourcelog.id_event-1]

                        # Add event to event log
                        self.add_event(activityName, caseName,
                                       time, stage,
                                       eventName, resourceName)
                    line_count = line_count+1
                # Sort the event list by event time
                self.events.eventList.sort()
                self.enrich_elements()

    def add_event(self, activityName, caseName,
                  time, stage,
                  eventName, resourceName) -> None:
        # Adds a single event to each list of the event log

        # Get IDs or add mandatory elements, get elements - except event
        activityID = self.activities.get_id_or_add(activityName)
        activity = self.activities.activityList[activityID]
        caseID = self.cases.get_id_or_add(caseName)
        case = self.cases.caseList[caseID]

        # Get IDs or add optional elements
        resourceID = None
        resource = None
        if resourceName is not None:
            resourceID = self.resources.get_id_or_add(resourceName)
            resource = self.resources.resourceList[resourceID]

        self.events.add_event(eventName, time, stage, activity, case, resource)

    def enrich_elements(self):
        eventID = 0
        for event in self.events.eventList:
            event.id = eventID
            # Get the relevant elements
            event.activity.enrich(event, event.case, event.resource)
            event.case.enrich(event, event.activity, event.resource)
            if event.resource is not None:
                event.resource.enrich(event, event.activity, event.case)
            eventID = eventID+1

    def analyse_paths(self):
        for case in self.cases.caseList:
            self.paths.add_case(case)
            self.pathtree.add_case(case)
