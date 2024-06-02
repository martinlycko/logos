# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt

# From standard library
from datetime import datetime

# From other modules
from ...shared_utils.eventtypes import EventType


class Event(BaseModel):
    # A class to capture a single event
    id: NonNegativeInt          # Generated, position in resources
    name: str | None = None     # Imported from the event log, if present

    # Timestamps of the event log
    time: datetime              # Timestamp of the event
    stage: EventType            # Lifecycle stage of event

    # References to other modules
    activity: NonNegativeInt | None = None      # Related activity ID
    case: NonNegativeInt | None = None          # Related case ID
    resource:  NonNegativeInt | None = None     # Related resource ID

    def enrich(self, caseID, activityID, resourceID) -> None:
        self.case = caseID
        self.resource = resourceID
        self.activity = activityID