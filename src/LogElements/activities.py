# For type safety and code quality
from pydantic import BaseModel, PositiveInt
from typing import List

# Reference to other event log classes
from LogElements.activity import Activity
from event_log import EventLog


class Activities(BaseModel):
    # A class to capture all activities
    activityList: List[Activity]    # A list of activities
    log: EventLog                   # Reference to the parent event log

    def add_activity(self, activity_name) -> None:
        # Adds an activity to the activity list
        new_activity = Activity(len(self.activityList+1),
                                activity_name, self.log)
        self.activity_list.append(new_activity)

    def get_id_if_in_list(self, name) -> PositiveInt | None:
        # Returns the ID of the activity with the given name
        # Returns None if no activity with the name has been found
        for activity in self.activityList:
            if activity.name == name:
                return activity.id
        return None

    def get_names(self) -> List[str]:
        # Returns an containing all activity names
        names: List[str] = []
        for activity in self.activityList:
            names.append(activity.name)
        return names

    def get_name(self, id) -> str:
        # Returns the name of an activity with provided ID
        return self.activityList[id].name
