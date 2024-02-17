from resource_event import Resource

class Resources:
    # A class to capture all resources
    
    resource_list = []      # A list of resource
    count = 0               # Incrementing counter to generate resource IDs

    def __init__(self) -> None:
        resource_list = []
        count = 0

    def add_resource(self, resource_name):
        self.count = self.count+1
        new_resource = Resource(self.count, resource_name)
        self.resource_list.append(new_resource)

    def get_id_if_in_list(self, name):
        resource_ID = -1
        for resource in self.resource_list:
            if resource.name == name:
                resource_ID = resource.id
        return resource_ID