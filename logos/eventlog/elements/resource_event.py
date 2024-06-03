# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt
from typing import List, Any


class Resource(BaseModel):
    # A class to capture a single case
    id: NonNegativeInt          # Generated, position in resources
    name: str                   # Imported from the event log

    # References to other elements, set as any to avoid circular import
    events: List[Any] = []       # List of related events
    activities: List[Any] = []   # List of related activities
    cases: List[Any] = []        # List of related cases

    def enrich(self, eventID, activityID, caseID) -> None:
        self.events.append(eventID)
        if activityID not in self.activities:
            self.activities.append(activityID)
        if caseID not in self.cases:
            self.cases.append(caseID)
