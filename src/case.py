from datetime import datetime

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
    
    def case_details(self):
        # Returns descriptions and details of a sigle case searched for using its original ID
        
        # Create a dictionary to return 
        case = {}
        case['original ID'] = self.id_original
        case['attributes'] = self.attributes
        case['path'] = []

        # Search the event log for events that relate to this case
        for event in self.log.events.event_list:
            if event.id_case == self.id_internal:
                case['path'].append(event)
        return case
    
    def turnaround_time(self):
        # Returns the throughput time for a case
        
        # Get a list of all events that relate to this event
        events = []
        for event in self.log.events.event_list:
            if event.id_case == self.id_internal:
                events.append(event)

        # Find the first event for this case
        first = datetime.strptime(events[0].time_end, "%d-%m-%Y:%H.%M")
        for event in events:
            if first > datetime.strptime(event.time_end, "%d-%m-%Y:%H.%M"):
                first = datetime.strptime(event.time_end, "%d-%m-%Y:%H.%M")

        # Find the last event for this case
        last = datetime.strptime(events[0].time_end, "%d-%m-%Y:%H.%M")
        for event in events:
            if last < datetime.strptime(event.time_end, "%d-%m-%Y:%H.%M"):
                last = datetime.strptime(event.time_end, "%d-%m-%Y:%H.%M")

        # Return the difference between the last and first event 
        return last - first