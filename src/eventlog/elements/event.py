# For type safety and code quality
from pydantic import BaseModel, PositiveInt
from datetime import datetime
from shared_utils.eventtypes import EventType

# Reference to event log class
from ..event_log import EventLog
from case import Case
from activity import Activity
from resource_event import Resource


class Event(BaseModel):
    # A class to capture a single event
    id: PositiveInt             # Generated, position in resources
    name: str | None = None     # Imported from the event log, if present

    # Timestamps of the event log
    time: datetime              # Timestamp of the event
    stage: EventType            # Lifecycle stage of event

    # References to other event log elements
    log: EventLog               # Reference to the parent event log
    cases: Case                 # List of related event IDs
    activities: Activity        # List of related activity IDs
    resources: Resource         # List of related resource IDs
