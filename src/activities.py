from activity import Activity

class Activities:
    # A class to capture all activities
    activity_list = []
    count = 0

    def __init__(self) -> None:
        activity_list = []
        count = 0

    def add_activity(self, activity_name):
        self.count = self.count+1
        new_activity = Activity(self.count, activity_name)
        self.activity_list.append(new_activity)