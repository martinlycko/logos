from case import Case
from datetime import datetime, timedelta

class Cases:
    # A class to capture all activities

    case_list = []      # A list of cases
    count = 0           # Incrementing counter to generate case IDs
    log = ""            # A reference to the event log in which this activity can be found

    def __init__(self, log) -> None:
        self.case_list = []
        self.count = 0
        self.log = log

    def add_case(self, id_original, attributes):
        self.count = self.count+1
        new_case = Case(self.count, id_original, attributes, self.log)
        self.case_list.append(new_case)

    def get_id_if_in_list(self, id_original):
        # Returns a result list with first value indicating if ID has been found, and the second value being the ID if it has been found
        result = [False, -1]
        for case in self.case_list:
            if case.id_original == id_original:
                result[0] = True
                result[1] = case.id_internal
                break
        return result
    
    def get_case_original_id(self, id):
        # Returns the case that matches the original ID
        result = [False, -1]
        for case in self.case_list:
            if case.id_original == id_original:
                result[0] = True
                result[1] = case
                break
        return result

    def get_case_internal_id(self, id):
        # Returns the case that matches the internal ID
        result = [False, -1]
        for case in self.case_list:
            if case.id_original == id_internal:
                result[0] = True
                result[1] = case
                break
        return result
    
    def turnaround_times(self):
        turnaround_times = {}
        for case in self.case_list:
            turnaround_times[case.id_original] = case.turnaround_time()
        return turnaround_times
    
    def case_with_min_turnaround_time(self):
        turnaround_times = self.turnaround_times()
        return min(turnaround_times.items(), key=lambda x: x[1])
    
    def case_with_max_turnaround_time(self):
        turnaround_times = self.turnaround_times()
        return max(turnaround_times.items(), key=lambda x: x[1])
    
    def avg_turnaround_time(self):
        turnaround_times = self.turnaround_times()
        return sum(turnaround_times.values(), timedelta()) / len(turnaround_times)