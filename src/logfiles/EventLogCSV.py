import os
import csv
from datetime import datetime

class EventLogCSV:
    
    # Set when creating the event log
    filepath = ""
    delimiter = ""
    
    # Three parts to each element - set with specific method
    # 1. False if not set, true if set
    # 2. If set (1st item == true), the column number (starting with 1) that contains this information 
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
    def __init__(self, filepath, delimiter, CaseID_Column, ActivityName_Column, CompletedTime_Column, CompletedTime_Format) -> None:
        self.set_FilePath(filepath, delimiter)
        self.set_ActivityName_Column(ActivityName_Column)
        self.set_CaseID_Column(CaseID_Column)
        self.set_CompletedTime_Column(CompletedTime_Column, CompletedTime_Format)

    def set_FilePath(self, filepath, delimiter):
        # Sets the filepath value if the file exists and is a CSV file
        if os.path.isfile(filepath) == False:
                raise FileNotFoundError('Cannot find event log in filepath')
        if filepath.endswith('.csv') == False:
                raise ValueError('Provided file is not a CSV file')
        self.filepath = filepath
        self.delimiter = delimiter
    
    def set_ActivityName_Column(self, ColumnNumber):
        # Sets the ActivityName column if the column exists and all values in the column are non-empty
        with open(self.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            for row in csv_reader:
                if len(row) < ColumnNumber:
                    raise ValueError('Column number for activities does not exist')
                if row[ColumnNumber-1] == '':
                    raise ValueError('One or more events do not have activity names')
        self.activity_name[0] = True
        self.activity_name[1] = ColumnNumber

    def set_CaseID_Column(self, ColumnNumber):
       # Sets the CaseID column if the column exists and all values in the column are non-empty
        with open(self.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            for row in csv_reader:
                if len(row) < ColumnNumber:
                    raise ValueError('Column number for Case IDs does not exist')
                if row[ColumnNumber-1] == '':
                    raise ValueError('One or more events do not have Case IDs')
        self.case_original_id[0] = True
        self.case_original_id[1] = ColumnNumber
    
    def set_CompletedTime_Column(self, ColumnNumber, Format):
        # Sets the FinishTime column if the column exists and all values can be converted into datetime format
        with open(self.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            line = 1
            for row in csv_reader:
                if line > 1:
                    if len(row) < ColumnNumber:
                        raise ValueError('Column number for Completion Times does not exist')
                    if row[ColumnNumber-1] == '':
                        raise ValueError('One or more events do not have Finish Times')
                    try:
                        timestamp = datetime.strptime(row[ColumnNumber-1], Format)
                    except ValueError:
                        raise ValueError('Not all datetime values match the provided format. Issue found in line: ' + str(line))
                line = line + 1
        self.time_completed[0] = True
        self.time_completed[1] = ColumnNumber
        self.time_completed[2] = Format
    
    def set_EventID_Column(self, ColumnNumber):
        # Sets the EventID column if the column exists and all values in the column are non-empty
        with open(self.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            for row in csv_reader:
                if len(row) < ColumnNumber:
                    raise ValueError('Column number does not exist')
                if row[ColumnNumber-1] == '':
                    raise ValueError('Empty EventID found')
        self.event_original_id[0] = True
        self.event_original_id[1] = ColumnNumber