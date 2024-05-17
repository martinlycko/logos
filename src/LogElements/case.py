# For type safety and code quality
from pydantic import BaseModel, PositiveInt
from typing import List, Dict, Any
from datetime import timedelta

# Reference to event log class
from event_log import EventLog
from event import Event
from activity import Activity
from resource_event import Resource


class Case(BaseModel):
    # A class to capture a single case
    id: PositiveInt             # Generated, position in cases
    name: str                   # Imported from the event log

    # The set of attributes is imported with the event log (e.g. price)
    attributes: None | Dict[str, Any]

    # References to other event log elements
    log: EventLog               # Reference to the parent event log
    events: List[Event]         # List of related event IDs
    activities: List[Activity]  # List of related activity IDs
    resources: List[Resource]   # List of related resource IDs

    def turnaround_time(self) -> timedelta:
        # Returns the difference between the first event's start time
        # and the last event's finish time
        return self.events[0].time_end - self.events[0].time_start
