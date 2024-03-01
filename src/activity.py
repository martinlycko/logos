class Activity:
    # A class to capture a single activity

    id = 0          # IDs are automatically generated, the ID-1 is the position in the activities list
    name = ""       # Names are imported from the event log (e.g. "Submit Order")

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

    def execution_count(self, activity_name):
        # Returns the number of times an activity has been executed
        return False
    
    def case_count(self, activity_name):
        # Returns the number of cases that an activity has been executed for
        return False
    
    def average_throughput_time(self, id_external):
        # Returns the throughput time for a single activity
        return False