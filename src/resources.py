from resource_event import Resource

class Resources:
    # A class to capture all resources
    resource_list = []
    count = 0

    def __init__(self) -> None:
        resource_list = []
        count = 0

    def add_resource(self, resource_name):
        self.count = self.count+1
        new_resource = Resource(self.count, resource_name)
        self.resource_list.append(new_resource)