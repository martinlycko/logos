# For type safety and code quality
from pydantic import BaseModel, PositiveInt
from typing import List

# Reference to event log class
from event_log import EventLog
from event import Event
from case import Case
from resource_event import Resource


class Activity(BaseModel):
    # A class to capture a single activity
    id: PositiveInt             # Generated, position in activities
    name: str                   # Imported from the event log

    # References to other event log elements
    log: EventLog               # Reference to the parent event log
    events: List[Event]         # List of related event IDs
    cases: List[Case]           # List of related case IDs
    resources: List[Resource]   # List of related resource IDs

    def count_exectution(self) -> PositiveInt:
        # Returns the number of times an activity has been executed
        return len(self.events)

    def count_cases(self) -> PositiveInt:
        # Returns the number of cases for which the activity was executed
        return len(self.cases)

    def count_resources(self) -> PositiveInt | None:
        # Returns the number of resources that execute this activity
        # Returns none if resources have not been captured in the log
        if self.log.resources.count == 0:
            return None
        else:
            return len(self.resources)
