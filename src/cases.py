from case import Case

class Cases:
    # A class to capture all activities

    case_list = []      # A list of cases
    count = 0           # Incrementing counter to generate case IDs

    def __init__(self) -> None:
        case_list = []
        count = 0

    def add_case(self, id_original, attributes):
        self.count = self.count+1
        new_case = Case(self.count, id_original, attributes)
        self.case_list.append(new_case)

    def get_id_if_in_list(self, id_original):
        case_ID = -1
        for case in self.case_list:
            if case.id_original == id_original:
                case_ID = case.id_internal
        return case_ID