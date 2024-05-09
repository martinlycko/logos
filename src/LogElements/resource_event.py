class Resource:
    # A class to capture a single case

    def __init__(self, id, name, log) -> None:
        # IDs are automatically generated, ID-1 is position in the list
        # Names are imported from the event log (e.g. employee names)
        # A reference to the event log in which this activity can be found
        self.id = id
        self.name = name
        self.log = log
