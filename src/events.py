from event import Event

class Events:
    # A class to capture all events
    
    event_list = []     # A list of events
    count = 0           # Incrementing counter to generate event IDs

    def __init__(self) -> None:
        event_list = []
        count = 0

    def add_event(self, id_original, starttime, endtime, case, activity, resource, attributes):
        self.count = self.count+1
        new_event = Event(self.count, id_original, starttime, endtime, case, activity, resource, attributes)
        self.event_list.append(new_event)

    def get_id_if_in_list(self, id_original):
        event_ID = -1
        for event in self.event_list:
            if event.id_original == id_original:
                event_ID = event.id_internal
                break
        return event_ID