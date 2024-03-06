import csv
from datetime import datetime

from events import Events
from cases import Cases
from activities import Activities
from resources import Resources

class EventLog:
    # A class to capture the entire event log structure
    
    # Each event log contains a list of events, cases, activities, and resources
    events = ""
    cases = ""
    activities = ""
    resources = ""

    def __init__(self) -> None:
        self.events = Events(self)
        self.cases = Cases(self)
        self.activities = Activities(self)
        self.resources = Resources(self)

    def add_event(self, original_event_id, original_case_id, finish_time, activity_name, resource_name):
        # Adds a single event to each list of the event log

        # Check/get IDs of the event, case, activity, and resource already in the log
        internal_event_id = self.events.get_id_if_in_list(original_event_id)
        internal_case_id = self.cases.get_id_if_in_list(original_case_id)
        internal_activity_id = self.activities.get_id_if_in_list(activity_name)
        internal_resource_id = self.resources.get_id_if_in_list(resource_name)
     
        # Add case to case list if not in there already
        if internal_case_id[0] == False:
            self.cases.add_case(original_case_id, [])

        # Add activity to activity list if not in there already
        if internal_activity_id[0] == False:
            self.activities.add_activity(activity_name)
        
        # Add resource to resource list if not in there already
        if internal_resource_id[0] == False:
            self.resources.add_resource(resource_name)
            
        # Get added IDS and add event to event list if not in there already
        internal_case_id = self.cases.get_id_if_in_list(original_case_id)
        internal_activity_id = self.events.get_id_if_in_list(activity_name)
        internal_resource_id = self.resources.get_id_if_in_list(resource_name)
        if internal_event_id[0] == False:
            self.events.add_event(original_event_id, "", finish_time, internal_case_id[1], internal_activity_id[1], internal_resource_id[1], [])

    def add_events_from_CSV(self, EventLogCSV):

        # Take a path to CSV file and let the user input the type of each column
        # Column types can be event ID, case ID, resource name, actvity name, finish time,...
        # Iterate over the csv file row by row
        # In each row, run the add_event function matching the columns to the parameters of the add_event function using the column types
        
        with open(EventLogCSV.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 1
            for row in csv_reader:
                if line_count == 1:
                    pass
                else:
                    # Collect all mandatory columns from the event log
                    event_original_id = row[EventLogCSV.event_original_id-1]
                    finish_time = datetime.strptime(row[EventLogCSV.finish_time-1], EventLogCSV.datetime_format)
                    case_original_id = row[EventLogCSV.case_original_id-1]
                    activity_name = row[EventLogCSV.activity_name-1]
                    
                    # If present, collect optionals with single column from event log
                    if EventLogCSV.start_time == 0:
                        start_time = ""
                    else:
                        start_time = datetime.strptime(row[EventLogCSV.start_time-1], EventLogCSV.datetime_format)

                    if EventLogCSV.resource_name == 0:
                        resource_name = ""
                    else:
                        resource_name = row[EventLogCSV.resource_name-1]

                    # If present, collect optionals with multiple columns from event log
                    event_attributes = ""
                    case_attributes = ""
                    
                    # Add event to event log
                    self.add_event(event_original_id, case_original_id, finish_time, activity_name, resource_name)
                line_count = line_count+1

    def shape(self):
        # Returns descriptive statistics about the event log
        return False