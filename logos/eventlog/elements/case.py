# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt

# From standard library
from datetime import timedelta


class Case(BaseModel):
    # A class to capture a single case
    id: NonNegativeInt             # Generated, position in cases
    name: str                   # Imported from the event log

    def turnaround_time(self) -> timedelta:
        # TO BE CHECKED
        # Returns the difference between the first event's received time
        # and the last event's completed time
        return self.events[0].time - self.events[0].received
