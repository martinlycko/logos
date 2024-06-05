# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt, PositiveInt
from typing import List, Any

# From other modules
from ...shared_utils.eventtypes import EventType


class Case(BaseModel):
    # A class to capture a single case
    id: NonNegativeInt              # Generated, position in cases
    name: str                       # Imported from the event log

    # References to other elements, set as any to avoid circular import
    events: List[Any] = []       # List of related, ordered events
    activities: List[Any] = []   # List of related activities
    resources: List[Any] = []    # List of related resources
    path: List[Any] = []         # List of related, ordered completion events

    def enrich(self, eventID, activityID, resourceID) -> None:
        self.events.append(eventID)
        if activityID not in self.activities:
            self.activities.append(activityID)
        if (resourceID is not None
                and resourceID not in self.resources):
            self.resources.append(resourceID)
        if eventID.stage is EventType.complete:
            self.path.append(activityID)

    def count_events(self) -> PositiveInt:
        # Returns the number of events a case is associated with
        return len(self.events)

    def count_activities(self) -> PositiveInt:
        # Returns the number of activities executed for a case
        return len(self.activities)

    def count_resources(self) -> PositiveInt | None:
        # Returns the number of resources that worked on this case
        # Returns none if resources have not been captured in the log
        if len(self.resources) == 0:
            return None
        else:
            return len(self.resources)
