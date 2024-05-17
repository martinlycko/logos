# For type safety and code quality
from pydantic import BaseModel, PositiveInt
from datetime import datetime

# Reference to event log class
from event_log import EventLog
from case import Case
from activity import Activity
from resource_event import Resource


class Event(BaseModel):
    # A class to capture a single event
    id: PositiveInt             # Generated, position in resources
    name: str | None = None     # Imported from the event log, if present

    # Timestamps of the event log
    received: datetime          # Same as previous events completed time
    ready: datetime | None      # Optional, when case is ready for processing
    start: datetime | None      # Optional, manual work starting
    stop: datetime | None       # Optional, manual work finished
    completed: datetime         # Release time of case, sent to next activity

    # References to other event log elements
    log: EventLog               # Reference to the parent event log
    cases: Case                 # List of related event IDs
    activities: Activity        # List of related activity IDs
    resources: Resource         # List of related resource IDs
