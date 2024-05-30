# For type safety and code quality
from pydantic import BaseModel, PositiveInt, NonNegativeInt
from typing import List

# Reference to other event log classes
from .activity import Activity


class Activities(BaseModel):
    # A class to capture all activities
    activityList: List[Activity] = []    # A list of activities

    def get_id(self, name) -> PositiveInt | None:
        # Returns the ID of the activity with the given name
        # Returns None if no activity with the name has been found
        for activity in self.activityList:
            if activity.name == name:
                return activity.id
        return None

    def add_activity(self, name) -> PositiveInt:
        # Adds an activity to the activity list and returns its ID
        new_activity = Activity(
            id=len(self.activityList),
            name=name
        )
        self.activityList.append(new_activity)
        return new_activity.id

    def get_id_or_add(self, name) -> PositiveInt:
        # Checks if teh activity is already in the activity list using its name
        ID = self.get_id(name)
        if ID is None:
            # Adds the activity and returns the newly created ID
            return self.add_activity(name)
        else:
            # Returns the ID of the existing activity in the list
            return ID

    def enrich_activity(self, name, eventID, caseID, resourceID) -> None:
        # Adds related elements to an activities' lists
        # Finds the ID of the activity by its name
        ID = self.get_id(name)
        # Updates its
        self.activityList[ID].events.append(eventID)
        self.activityList[ID].events.append(caseID)
        self.activityList[ID].events.append(resourceID)

    def get_name(self, id) -> str:
        # Returns the name of an activity with provided ID
        return self.activityList[id].name

    def get_names(self) -> List[str]:
        # Returns an containing all activity names
        names: List[str] = []
        for activity in self.activityList:
            names.append(activity.name)
        return names

    def count(self) -> NonNegativeInt:
        return len(self.activityList)
