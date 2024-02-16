class Resource:
    # A class to capture a single case
    
    id = 0          # IDs are automatically generated, the ID-1 is the position in the resource list
    name = ""       # Names are imported from the event log (e.g. employee names)

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name