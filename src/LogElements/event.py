class Event:
    # A class to capture a single event

    def __init__(self, id_internal, id_original, starttime, endtime, case,
                 activity, resource, attributes, log) -> None:
        # Internal IDs are automatically generated, ID-1 is positon in list
        # Original IDs are imported from the event log
        # Start times may be empty or imported from the event log
        # End times are imported from the event log
        # Case IDs are picked up from the event log
        # Activity IDs are picked up from the event log
        # Resource IDs are picked up from the event log
        # Optinal list of event related attributes (e.g. cost to process event)
        # A reference to the event log in which this activity can be found
        self.id_internal = id_internal
        self.id_original = id_original
        self.time_start = starttime
        self.time_end = endtime
        self.id_case = case
        self.id_activity = activity
        self.id_resource = resource
        self.attributes = attributes
        self.log = log
