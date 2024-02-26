import csv

from events import Events
from cases import Cases
from activities import Activities
from resources import Resources

class EventLog:
    # A class to capture the entire event log structure
    
    # Each event log contains a list of events, cases, activities, and resources
    events = Events()
    cases = Cases()
    activities = Activities()
    resources = Resources()

    def __init__(self) -> None:
        self.events = Events()
        self.cases = Cases()
        self.activities = Activities()
        self.resources = Resources()

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

    def add_events_from_CSV(self, path, column_types):

        # Take a path to CSV file and let the user input the type of each column
        # Column types can be event ID, case ID, resource name, actvity name, finish time,...
        # Iterate over the csv file row by row
        # In each row, run the add_event function matching the columns to the parameters of the add_event function using the column types
        
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 1
            for row in csv_reader:
                if line_count == 1:
                    pass
                else:
                    self.add_event(row[1], row[0], row[2], row[3], row[4])
                line_count = line_count+1

    def shape(self):
        # Returns descriptive statistics about the event log
        return False
    
    def activity_execution_count(self, activity_name):
        # Returns the number of times an activity has been executed
        return False
    
    def activity_case_count(self, activity_name):
        # Returns the number of cases that an activity has been executed for
        return False
    
    def activity_throughput_time(self, id_external):
        # Returns the throughput time for a single activity
        return False
    
    def case_details_with_external_ID(self, id_external):
        # Returns descriptions and details of a sigle case
        return False
    
    def case_throughput_time(self, id_external):
        # Returns the throughput time for a single case
        return False