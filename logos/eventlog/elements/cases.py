# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt
from typing import List

# From standard library
from datetime import timedelta

# Reference to other event log classes
from .case import Case


class Cases(BaseModel):
    # A class to capture all activities
    caseList: List[Case] = []   # A list of cases

    def get_id(self, name) -> NonNegativeInt | None:
        # Returns the ID of the case with the given name
        # Returns None if no case with the name has been found
        for case in self.caseList:
            if case.name == name:
                return case.id
        return None

    def add_case(self, name) -> NonNegativeInt:
        # Adds a case to the case list and returns its ID
        new_case = Case(
            id=len(self.caseList),
            name=name
        )
        self.caseList.append(new_case)
        return new_case.id

    def get_id_or_add(self, name) -> NonNegativeInt:
        # Checks if the case is already in the case list using its name
        ID = self.get_id(name)
        if ID is None:
            # Adds the case and returns the newly created ID
            return self.add_case(name)
        else:
            # Returns the ID of the existing case in the list
            return ID

    def count(self) -> NonNegativeInt:
        return len(self.caseList)

    def get_names(self) -> List[str]:
        # Returns a list containing all case names
        names: List[str] = []
        for case in self.caseList:
            names.append(case.name)
        return names

    # def turnaround_times
    # Gets the turnaround times of all cases

    def turnaround_time_min(self) -> Case:
        # TO BE CHECKED
        # Returns the case with the smallest turnaround time
        turnaround_times = self.turnaround_times()
        return min(turnaround_times.items(), key=lambda x: x[1])

    def turnaround_time_max(self) -> Case:
        # TO BE CHECKED
        # Returns the case with the fastest turnaround time
        turnaround_times = self.turnaround_times()
        return max(turnaround_times.items(), key=lambda x: x[1])

    def turnaround_time_avg(self) -> timedelta:
        # TO BE CHECKED
        # Returns the average turnaround time of all cases
        turnaround_times = self.turnaround_times()
        return (sum(turnaround_times.values(), timedelta())
                / len(turnaround_times))
