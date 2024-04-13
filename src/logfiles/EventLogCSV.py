import os
import csv

class EventLogCSV:
    
    # Set when creating the event log
    filepath = ""
    delimiter = ""
    
    # Three parts to each element - set with specific method
    # 1. False if not set, true if set
    # 2. If set (1st item == true), the column number (starting with 0) that contains this information 
    # 3. For datetime element, the format in which they are set
    event_original_id = [False, 0]
    event_attributes = [False, 0]
    time_received = [False, 0, ""]
    time_ready = [False, 0, ""]
    time_start = [False, 0, ""]
    time_stop = [False, 0, ""]
    time_completed = [False, 0, ""]
    activity_name = [False, 0]
    case_original_id = [False, 0]
    case_attributes = [False, 0]
    resource_name = [False, 0]

    # Sets all mandatory event log elements
    def __init__(self, filepath, delimiter, EventID_Column, CaseID_Column, CompletedTime_Column, FinishTime_Format) -> None:
        self.set_FilePath(filepath, delimiter)
        self.set_EventID_Column(EventID_Column)
        self.set_CaseID_Column(CaseID_Column)
        self.set_FinishTime_Column(CompletedTime_Column, FinishTime_Format)

    def set_FilePath(self, filepath, delimiter):
        # Sets the filepath value if the file exists and is a CSV file
        if os.path.isfile(filepath) == False:
                raise FileNotFoundError('Cannot find event log in filepath')
        if filepath.endswith('.csv') == False:
                raise ValueError('Provided file is not a CSV file')
        self.filepath = filepath
        self.delimiter = delimiter

    def set_EventID_Column(self, ColumnNumber):
        # Sets the EventID column if the column exists and all values in the column are non-empty
        with open(self.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, self.delimiter)
            for row in csv_reader:
                if first_line.count(self.delimiter) + 1 < ColumnNumber:
                    raise ValueError('Column number does not exist')

    
    def set_CaseID_Column(self, ColumnNumber):
       # Sets the CaseID column if the column exists and all values in the column are non-empty
        return 0
    
    def set_FinishTime_Column(self, ColumnNumber, Format):
        # Sets the FinishTime column if the column exists and all values can be converted into datetime format
        return 0