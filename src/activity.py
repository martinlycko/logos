class Activity:
    # A class to capture a single activity

    id = 0          # IDs are automatically generated, the ID-1 is the position in the activities list
    name = ""       # Names are imported from the event log (e.g. "Submit Order")

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name