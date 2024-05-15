# For type safety and code quality
from pydantic import BaseModel, PositiveInt
from typing import List, Dict, Any

# Reference to event log class
from event_log import EventLog


class Case(BaseModel):
    # A class to capture a single case
    id: PositiveInt                 # Generated, position in cases
    name: str                       # Imported from the event log

    # The set of attributes is imported with the event log (e.g. price)
    attributes: None | Dict[str, Any]

    # References to other event log elements
    log: EventLog                   # Reference to the parent event log
    events: List[PositiveInt]       # List of related event IDs
    activities: List[PositiveInt]   # List of related activity IDs
    resources: List[PositiveInt]    # List of related resource IDs

    def __str__(self) -> str:
        case_number = ("Case: " + str(self.id_original) + " (internally id: "
                       + str(self.id_internal) + ")")

        case_attributes = ""
        if not self.attributes:
            case_attributes = "\nNo attributes"
        # Need to add attributes to print

        case_path = ""
        for event in self.log.events.event_list:
            if event.id_case == self.id_internal:
                case_path = (case_path + "\n"
                             + str(event.time_end)
                             + ": "
                             + self.log.activities.get_name(event.id_activity)
                             + ", "
                             + self.log.resources.get_name(event.id_resource))

        return case_number + case_attributes + case_path

    def case_details(self):
        # Returns descriptions and details of a sigle case
        # searched for using its original ID

        # ToDo: Create a dictionary to return
        case = {}
        case['original ID'] = self.id_original
        case['attributes'] = self.attributes
        case['path'] = []

        # Search the event log for events that relate to this case
        # ToDo: Need to make sure these are sorted chronologically
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
        first = events[0].time_end
        for event in events:
            if first > event.time_end:
                first = event.time_end

        # Find the last event for this case
        last = events[0].time_end
        for event in events:
            if last < event.time_end:
                last = event.time_end

        # Return the difference between the last and first event
        return last - first
