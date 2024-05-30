import csv
from datetime import datetime

from elements.events import Events
from elements.cases import Cases
from elements.activities import Activities
from elements.resources import Resources


class EventLog:
    # A class to capture the entire event log structure

    def __init__(self) -> None:
        # Each event log contains a list of
        # events, cases, activities, resources
        self.events = Events(self)
        self.cases = Cases(self)
        self.activities = Activities(self)
        self.resources = Resources(self)

    def add_event(self, original_event_id, original_case_id, finish_time,
                  activity_name, resource_name):
        # Adds a single event to each list of the event log

        # Check/get IDs of the event, case, activity, and resource
        # already in the log
        internal_event_id = self.events.get_id_if_in_list(original_event_id)
        internal_case_id = self.cases.get_id_if_in_list(original_case_id)
        internal_activity_id = self.activities.get_id_if_in_list(activity_name)
        internal_resource_id = self.resources.get_id_if_in_list(resource_name)

        # Add case to case list if not in there already
        if internal_case_id[0] is False:
            self.cases.add_case(original_case_id, [])

        # Add activity to activity list if not in there already
        if internal_activity_id[0] is False:
            self.activities.add_activity(activity_name)

        # Add resource to resource list if not in there already
        if internal_resource_id[0] is False:
            self.resources.add_resource(resource_name)

        # Get added IDs and add event to event list if not in there already
        internal_case_id = self.cases.get_id_if_in_list(original_case_id)
        internal_activity_id = self.activities.get_id_if_in_list(activity_name)
        internal_resource_id = self.resources.get_id_if_in_list(resource_name)
        if internal_event_id[0] is False:
            self.events.add_event(original_event_id, "", finish_time,
                                  internal_case_id[1], internal_activity_id[1],
                                  internal_resource_id[1], [])

    def add_events_from_CSV(self, EventLogCSV):
        # Imports an entire CSV event file row by row via add_event function
        # Requires a CSV file with the additional information
        # specified in the EventLogCSV class

        # Open the CSV file with its specified path
        with open(EventLogCSV.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=EventLogCSV.delimiter)
            line_count = 1
            for row in csv_reader:
                # Ignore the first row commonly including hearders
                if line_count == 1:
                    pass
                else:
                    # Collect all mandatory columns from the event log
                    event_original_id = row[EventLogCSV.event_original_id
                                            .getValue()-1]
                    finish_time = datetime.strptime(
                        row[EventLogCSV.time_completed.getValue()-1],
                        EventLogCSV.time_completed.getFormat())
                    case_original_id = row[EventLogCSV.case_original_id
                                           .getValue()-1]
                    activity_name = row[EventLogCSV.activity_name.getValue()-1]

                    # If present in the CSV file,
                    # collect the optional resource name of each events
                    if EventLogCSV.resource_name.isSet is False:
                        resource_name = ""
                    else:
                        resource_name = row[EventLogCSV.resource_name
                                            .getValue()-1]

                    # Add event to event log
                    self.add_event(event_original_id, case_original_id,
                                   finish_time, activity_name, resource_name)
                line_count = line_count+1

    def shape(self):
        # Returns descriptive statistics about the event log
        return False