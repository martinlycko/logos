# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt
from typing import List


class Resource(BaseModel):
    # A class to capture a single case
    id: NonNegativeInt          # Generated, position in resources
    name: str                   # Imported from the event log

    # References to other elements in the model
    events: List[NonNegativeInt] = []       # List of related event IDs
    activities: List[NonNegativeInt] = []   # List of related activity IDs
    cases: List[NonNegativeInt] = []        # List of related case ID

    def enrich(self, eventID, activityID, caseID) -> None:
        self.events.append(eventID)
        if activityID not in self.activities:
            self.activities.append(activityID)
        if caseID not in self.cases:
            self.cases.append(caseID)
