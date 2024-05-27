# For type safety and code quality
from pydantic import BaseModel, PositiveInt
from typing import List

# Reference to other event log classes
from resource_event import Resource
from ..event_log import EventLog


class Resources(BaseModel):
    # A class to capture all resources
    resoruceList: List[Resource]    # A list of resources
    log: EventLog                   # Reference to the parent event log

    def add_resource(self, resource_name) -> None:
        new_resource = Resource(len(self.resoruceList)+1,
                                resource_name, self.log)
        self.resource_list.append(new_resource)

    def get_id(self, name) -> PositiveInt | None:
        # Returns the ID of the activity with the given name
        # Returns None if no activity with the name has been found
        for case in self.resoruceList:
            if case.id == name:
                return case.id
        return None

    def get_name(self, id) -> str:
        return self.resource_list[id].name
