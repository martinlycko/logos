from case import Case

class Cases:
    # A class to capture all activities

    case_list = []      # A list of cases
    count = 0           # Incrementing counter to generate case IDs

    def __init__(self) -> None:
        case_list = []
        count = 0

    def add_case(self, case_attributes):
        self.count = self.count+1
        new_case = Case(self.count, case_attributes)
        self.case_list.append(new_case)