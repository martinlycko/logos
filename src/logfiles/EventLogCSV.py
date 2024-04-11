class EventLogCSV:
    filepath = ""
    event_original_id = 0
    event_attributes = 0
    start_time = 0
    finish_time = 0
    activity_name = 0
    case_original_id = 0
    case_attributes = 0
    resource_name = 0
    datetime_format = ""

    def __init__(self, path) -> None:
        self.filepath = path
    
    def validate(self) -> None:
        # Initialises a new column structure for an event log csv file
        # Event IDs, finish times, case IDs, and activity names need to be set to a single integer value
        # Start-times and resource names are optional. Can be 0 if not in the file or a single integer with its column number
        # Event attributes and case attributes are optional. Can be 0, single integer value, or a list of integers for more than 1 column with attributes
        # Datetime format consitent with datetime.strptime requirements
        return True