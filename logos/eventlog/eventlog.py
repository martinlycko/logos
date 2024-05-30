# For type safety and code quality
from pydantic import BaseModel, PositiveInt
from typing import List

# From standard library
import csv
from datetime import datetime

# Reference to other event log classes
from logos.eventlog.elements.activities import Activities
from logos.eventlog.elements.cases import Cases

# Import of supported adapter classes for source logs
from logos.adapters.EventLogCSV import EventLogCSV


class EventLog(BaseModel):
    # A class to capture the entire event log structure
    activities: Activities = Activities()   # Contains a list of all activities
    cases: Cases = Cases()                  # Contains a list of all cases

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

                        # Add event to event log
                        self.add_event(activityName, caseName)
                    line_count = line_count+1

    def add_event(self, activityName, caseName) -> None:
        # Adds a single event to each list of the event log

        # Check/get IDs of the event, case, activity, and resource
        # already in the log
        activityID = self.activities.get_id_or_add(activityName)
        caseID = self.cases.get_id_or_add(caseName)
