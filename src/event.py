class Event:
    # A class to capture a single event
    
    id = 0              # IDs may be imported from the event log or automatically generated, ID-1 should be the positon in the events list
    time_start = 0      # Start times may be empty or imported from the event log
    time_end = 0        # End times are imported from the event log
    id_case = 0         # Case IDs are picked up from the event log and need to correspond to those in the cases list
    id_activity = 0     # Activity IDs are picked up from the event log and need to correspond to those in the activities list
    id_resource = 0     # Resource IDs are picked up from the event log and need to correspond to those in the resource list
    attributes = {}     # Optinal list of event related attributes (e.g. cost to process this event)

    def __init__(self, id, starttime, endtime, case, activity, resource, attributes) -> None:
        self.id = id
        self.time_start = starttime
        self.time_end = endtime
        self.id_case = case
        self.id_activity = activity
        self.id_resource = resource
        self.attributes = attributes