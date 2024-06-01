# For type safety and code quality
from pydantic import BaseModel, PositiveInt, NonNegativeInt
from typing import List


class Activity(BaseModel):
    # A class to capture a single activity
    id: NonNegativeInt  # Generated, position in activities
    name: str           # Imported from the event log

    # References to other elements in the model
    events: List[NonNegativeInt] = []       # List of related event IDs
    cases: List[NonNegativeInt] = []        # List of related case IDs
    resources: List[NonNegativeInt] = []    # List of related resource IDs

    def enrich(self, eventID, caseID, resourceID) -> None:
        self.events.append(eventID)
        if caseID in self.cases is False:
            self.cases.append(caseID)
        if (resourceID in self.resources is False
                and resourceID is not None):
            self.cases.append(resourceID)

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