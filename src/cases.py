from case import Case

class Cases:
    # A class to capture all activities

    case_list = []      # A list of cases
    count = 0           # Incrementing counter to generate case IDs

    def __init__(self) -> None:
        case_list = []
        count = 0

    def add_case(self, id, case_attributes):
        self.count = self.count+1
        new_case = Case(id, case_attributes)
        self.case_list.append(new_case)

    def check_if_in_list(self, id):
        in_list = False
        for case in self.case_list:
            if case.id == id:
                in_list = True
        return in_list