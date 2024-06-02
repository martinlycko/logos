# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt
from typing import List

# From standard library
from datetime import timedelta


class Case(BaseModel):
    # A class to capture a single case
    id: NonNegativeInt              # Generated, position in cases
    name: str                       # Imported from the event log

    # References to other elements in the model
    events: List[NonNegativeInt] = []       # List of related event IDs
    activities: List[NonNegativeInt] = []   # List of related activity IDs
    resources: List[NonNegativeInt] = []    # List of related resource ID

    def enrich(self, eventID, activityID, resourceID) -> None:
        self.events.append(eventID)
        if activityID not in self.activities:
            self.activities.append(activityID)
        if (resourceID is not None
                and resourceID not in self.resources):
            self.resources.append(resourceID)

    def turnaround_time(self) -> timedelta:
        # TO BE CHECKED
        # Returns the difference between the first event's received time
        # and the last event's completed time
        return self.events[0].time - self.events[0].received
