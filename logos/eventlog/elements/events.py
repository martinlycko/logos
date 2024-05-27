# For type safety and code quality
from pydantic import BaseModel, PositiveInt
from typing import List

# Reference to other event log classes
from event import Event
from ..event_log import EventLog


class Events(BaseModel):
    # A class to capture all events
    eventList: List[Event]    # A list of events
    log: EventLog             # Reference to the parent event log

    def add_event(self, name, time, case,
                  activity, resource, attributes):
        new_event = Event(len(self.activityList)+1, name, time, case,
                          activity, resource, attributes, self.log)
        self.event_list.append(new_event)

    def get_id(self, name) -> PositiveInt | None:
        # Returns the ID of the activity with the given name
        # Returns None if no activity with the name has been found
        for event in self.eventList:
            if event.name == name:
                return event.id
        return None
