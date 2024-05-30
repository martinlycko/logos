# For type safety and code quality
from pydantic import BaseModel, PositiveInt, NonNegativeInt


class Activity(BaseModel):
    # A class to capture a single activity
    id: NonNegativeInt             # Generated, position in activities
    name: str                   # Imported from the event log

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