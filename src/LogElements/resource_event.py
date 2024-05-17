# For type safety and code quality
from pydantic import BaseModel, PositiveInt
from typing import List

# Reference to event log class
from event_log import EventLog
from event import Event
from case import Case
from activity import Activity


class Resource(BaseModel):
    # A class to capture a single case
    id: PositiveInt             # Generated, position in resources
    name: str                   # Imported from the event log

    # References to other event log elements
    log: EventLog               # Reference to the parent event log
    events: List[Event]         # List of related event IDs
    cases: List[Case]           # List of related case IDs
    activities: List[Activity]  # List of related activity IDs
