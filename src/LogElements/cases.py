from case import Case
from datetime import datetime, timedelta


class Cases:
    # A class to capture all activities

    def __init__(self, log) -> None:
        # A list of cases
        # Incrementing counter to generate case IDs
        # A reference to the event log in which this activity can be found
        self.case_list = []
        self.count = 0
        self.log = log

    def add_case(self, id_original, attributes):
        self.count = self.count+1
        new_case = Case(self.count, id_original, attributes, self.log)
        self.case_list.append(new_case)

    def get_id_if_in_list(self, id_original):
        # Returns a result list with first value indicating if ID is found,
        # and the second value being the ID if it has been found
        result = [False, -1]
        for case in self.case_list:
            if case.id_original == id_original:
                result[0] = True
                result[1] = case.id_internal
                break
        return result

    def get_case_original_id(self, id_original):
        # Returns the case that matches the original ID,
        # a false in the tuple if the ID was not found
        # ToDo: Function needs testing
        result = [False, -1]
        for case in self.case_list:
            if case.id_original == id_original:
                result[0] = True
                result[1] = case
                break
        return result

    def get_case_internal_id(self, id_internal):
        # Returns the case that matches the internal ID,
        # a false in the tuple if the ID was not found
        # ToDo: Function needs testing
        result = [False, -1]
        for case in self.case_list:
            if case.id_internal == id_internal:
                result[0] = True
                result[1] = case
                break
        return result

    def turnaround_times(self):
        # Returns a dictionary of case IDs and turnaround times
        # ToDo: Test function with an list of cases
        turnaround_times = {}
        for case in self.case_list:
            turnaround_times[case.id_original] = case.turnaround_time()
        return turnaround_times

    def case_with_min_turnaround_time(self):
        # Returns the case with the smallest turnaround time
        turnaround_times = self.turnaround_times()
        return min(turnaround_times.items(), key=lambda x: x[1])

    def case_with_max_turnaround_time(self):
        # Returns the case with the fastest turnaround time
        turnaround_times = self.turnaround_times()
        return max(turnaround_times.items(), key=lambda x: x[1])

    def avg_turnaround_time(self):
        # Returns the average turnaround time of each case
        turnaround_times = self.turnaround_times()
        return (sum(turnaround_times.values(), timedelta())
                / len(turnaround_times))
