from event import Event


class Events:
    # A class to capture all events

    def __init__(self, log) -> None:
        # A list of events
        # Incrementing counter to generate event IDs
        # A reference to the event log in which this activity can be found
        self.event_list = []
        self.count = 0
        self.log = log

    def add_event(self, id_original, starttime, endtime, case,
                  activity, resource, attributes):
        self.count = self.count+1
        new_event = Event(self.count, id_original, starttime, endtime, case,
                          activity, resource, attributes, self.log)
        self.event_list.append(new_event)

    def get_id_if_in_list(self, id_original):
        # Returns a result list with first value indicating if ID is found,
        # and the second value being the ID if it has been found
        result = [False, -1]
        for event in self.event_list:
            if event.id_original == id_original:
                result[0] = True
                result[1] = event.id_internal
                break
        return result
