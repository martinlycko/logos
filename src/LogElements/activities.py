from LogElements.activity import Activity


class Activities:
    # A class to capture all activities

    def __init__(self, log) -> None:
        self.activity_list = []  # A list of activities
        self.count = 0           # Incrementing counter to activity IDs
        self.log = log           # A reference to the parent log

    def add_activity(self, activity_name):
        self.count = self.count+1
        new_activity = Activity(self.count, activity_name, self.log)
        self.activity_list.append(new_activity)

    def get_id_if_in_list(self, name):
        # Returns a result list with first value indicating if ID has been
        # found, and the second value being the ID if it has been found
        result = [False, -1]
        for activity in self.activity_list:
            if activity.name.isSet is True:
                if activity.name.getValue() == name:
                    result[0] = True
                    result[1] = activity.id
                    break
        return result

    def get_names(self):
        names = []
        for activity in self.activity_list:
            names.append(activity.name)
        return names

    def get_name(self, id):
        return self.activity_list[id].name.getValue()
