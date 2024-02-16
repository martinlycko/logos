class Event:
    # A class to capture a single event
    id = 0
    time_start = 0
    time_end = 0
    id_case = 0
    id_activity = 0
    id_resource = 0
    attributes = {}

    def __init__(self, id, starttime, endtime, case, activity, resource, attributes) -> None:
        self.id = id
        self.time_start = starttime
        self.time_end = endtime
        self.id_case = case
        self.id_activity = activity
        self.id_resource = resource
        self.attributes = attributes