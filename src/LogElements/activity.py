from utils.Optional import Optional


class Activity:
    # A class to capture a single activity

    def __init__(self, id, name, log) -> None:
        # IDs are automatically generated, ID-1 is the position in list
        # Names are imported from the event log (e.g. "Submit Order")
        # A reference to the event log in which this activity can be found
        self.id = Optional(id)
        self.name = Optional(name)
        self.log = log

    def execution_count(self, activity_name):
        # Returns the number of times an activity has been executed
        return False

    def case_count(self, activity_name):
        # Returns the number of cases that an activity has been executed for
        return False

    def average_throughput_time(self, id_external):
        # Returns the throughput time for a single activity
        return False
