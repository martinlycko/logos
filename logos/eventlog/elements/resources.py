# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt
from typing import List

# Reference to other event log classes
from .resource_event import Resource


class Resources(BaseModel):
    # A class to capture all resources
    resourceList: List[Resource] = []    # A list of resources

    def get_id(self, name) -> NonNegativeInt | None:
        # Returns the ID of the resource with the given name
        # Returns None if no resource with the name has been found
        for resource in self.resourceList:
            if resource.name == name:
                return resource.id
        return None

    def add_resource(self, name) -> NonNegativeInt:
        # Adds a resource to the resource list and returns its ID
        new_resource = Resource(
            id=len(self.resourceList),
            name=name
        )
        self.resourceList.append(new_resource)
        return new_resource.id

    def get_id_or_add(self, name) -> NonNegativeInt:
        # Checks if the resource is already in the list using its name
        ID = self.get_id(name)
        if ID is None:
            # Adds the resource and returns the newly created ID
            return self.add_resource(name)
        else:
            # Returns the ID of the existing resource in the list
            return ID

    def count(self) -> NonNegativeInt:
        return len(self.resourceList)

    def get_names(self) -> List[str]:
        # Returns a list containing all resource names
        names: List[str] = []
        for resource in self.resourceList:
            names.append(resource.name)
        return names
