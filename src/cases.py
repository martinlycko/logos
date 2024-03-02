from case import Case

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