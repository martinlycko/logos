# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt
from typing import List

# Reference to other event log classes
from .event import Event


class Events(BaseModel):
    # A class to capture all events
    eventList: List[Event] = []    # A list of events

    def get_id(self, name) -> NonNegativeInt | None:
        # Returns the ID of the event with the given name
        # Returns None if no event with the name has been found
        for event in self.eventList:
            if event.name == name:
                return event.id
        return None

    def add_event(self, name, time, stage) -> NonNegativeInt:
        # Adds a event to the event list and returns its ID
        new_event = Event(
            id=len(self.eventList),
            name=name,
            time=time,
            stage=stage
        )
        self.eventList.append(new_event)
        return new_event.id

    def count(self) -> NonNegativeInt:
        return len(self.eventList)

    def get_names(self) -> List[str]:
        # Returns a list containing all event names
        names: List[str] = []
        for event in self.eventList:
            if event.name is not None:
                names.append(event.name)
        return names
