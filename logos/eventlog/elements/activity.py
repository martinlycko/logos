# For type safety and code quality
from pydantic import BaseModel, PositiveInt, NonNegativeInt
from typing import List, Any


class Activity(BaseModel):
    # A class to capture a single activity
    id: NonNegativeInt  # Generated, position in activities
    name: str           # Imported from the event log

    # References to other elements, set as any to avoid circular import
    events: List[Any] = []       # List of related events
    cases: List[Any] = []        # List of related cases
    resources: List[Any] = []    # List of related resources

    def enrich(self, eventID, caseID, resourceID) -> None:
        self.events.append(eventID)
        if caseID not in self.cases:
            self.cases.append(caseID)
        if (resourceID is not None
                and resourceID not in self.resources):
            self.resources.append(resourceID)

    def count_events(self) -> PositiveInt:
        # Returns the number of times an activity has been executed
        return len(self.events)

    def count_cases(self) -> PositiveInt:
        # Returns the number of cases for which the activity was executed
        return len(self.cases)

    def count_resources(self) -> PositiveInt | None:
        # Returns the number of resources that execute this activity
        # Returns none if resources have not been captured in the log
        if len(self.resources) == 0:
            return None
        else:
            return len(self.resources)

