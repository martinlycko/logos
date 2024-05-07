from resource_event import Resource

class Resources:
    # A class to capture all resources
    
    resource_list = []      # A list of resource
    count = 0               # Incrementing counter to generate resource IDs
    log = ""

    def __init__(self, log) -> None:
        self.resource_list = []
        self.count = 0
        self.log = log

    def add_resource(self, resource_name):
        self.count = self.count+1
        new_resource = Resource(self.count, resource_name, self.log)
        self.resource_list.append(new_resource)

    def get_id_if_in_list(self, name):
        # Returns a result list with first value indicating if ID has been found, and the second value being the ID if it has been found
        result = [False, -1]
        for resource in self.resource_list:
            if resource.name == name:
                result[0] = True
                result[1] = resource.id
                break
        return result
    
    def get_names(self):
        names = []
        for resource in self.resource_list:
            names.append(resource.name)
        return names
    
    def get_name(self, id):
        return self.resource_list[id].name