# For type safety and code quality
from pydantic import BaseModel, PositiveInt
from typing import List

# From standard library
from datetime import timedelta

# Reference to other event log classes
from case import Case
from ..event_log import EventLog


class Cases(BaseModel):
    # A class to capture all activities
    caseList: List[Case]    # A list of cases
    log: EventLog           # Reference to the parent event log

    def add_case(self, name, attributes) -> None:
        new_case = Case(len(self.caseList+1),
                        name, attributes)
        self.caseList.append(new_case)

    def get_id(self, name) -> PositiveInt | None:
        # Returns the ID of the activity with the given name
        # Returns None if no activity with the name has been found
        for case in self.caseList:
            if case.id == name:
                return case.id
        return None

    def get_name(self, id) -> str:
        # Returns the name of an activity with provided ID
        return self.caseList[id].name

    def turnaround_time_min(self) -> PositiveInt:
        # Returns the case with the smallest turnaround time
        turnaround_times = self.turnaround_times()
        return min(turnaround_times.items(), key=lambda x: x[1])

    def turnaround_time_max(self) -> PositiveInt:
        # Returns the case with the fastest turnaround time
        turnaround_times = self.turnaround_times()
        return max(turnaround_times.items(), key=lambda x: x[1])

    def turnaround_time_avg(self) -> timedelta:
        # Returns the average turnaround time of each case
        turnaround_times = self.turnaround_times()
        return (sum(turnaround_times.values(), timedelta())
                / len(turnaround_times))
