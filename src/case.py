class Case:
    # A class to capture a single case

    id_internal = 0     # Internal IDs are automatically generated, the ID-1 is the position in the activities list
    id_original = 0     # Original IDs are imported from the event log
    attributes = {}     # The set of attributes is imported with the event log (e.g. price for a product)
    log = ""            # A reference to the event log in which this activity can be found

    def __init__(self, id_internal, id_original, attributes, log) -> None:
        self.id_internal = id_internal
        self.id_original = id_original
        self.attributes = attributes
        self.log = log
    
    def case_details(self, id_external):
        # Returns descriptions and details of a sigle case
        return False
    
    def turnaround_time(self, id_external):
        # Returns the throughput time for a single case
        return False