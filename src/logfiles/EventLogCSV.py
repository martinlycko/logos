import os
import csv
from datetime import datetime

class ColumnsSet:
    isSet = False
    Value = 0

    def __init__(self):
        self.isSet = False
        self.Value = 0

    def setValue(self, Value):
        self.isSet = True
        self.Value = Value

    def getValue(self):
        if self.isSet == True:
            return self.Value
        else:
            raise ValueError('Column not set')

class DateColumnValueSet:
    isSet = False
    Value = 0
    Format = ""

    def __init__(self):
        self.isSet = False
        self.Value = 0
        self.Format = ""

    def setValue(self, Value, Format):
        self.isSet = True
        self.Value = Value
        self.Format = Format

    def getValue(self):
        if self.isSet == True:
            return self.Value
        else:
            raise ValueError('Column not set')
        
    def getFormat(self):
        if self.isSet == True:
            return self.Format
        else:
            raise ValueError('Column not set')

class EventLogCSV:
    
    # Set when creating the event log
    filepath = ""
    delimiter = ""
    
    # Three parts to each element - set with specific method
    # 1. False if not set, true if set
    # 2. If set (1st item == true), the column number (starting with 1) that contains this information 
    # 3. For datetime element, the format in which they are set
    event_original_id = ColumnsSet()
    event_attributes = ColumnsSet()
    time_received = DateColumnValueSet()
    time_ready = DateColumnValueSet()
    time_start = DateColumnValueSet()
    time_stop = DateColumnValueSet()
    time_completed = DateColumnValueSet()
    activity_name = ColumnsSet()
    case_original_id = ColumnsSet()
    case_attributes = ColumnsSet()
    resource_name = ColumnsSet()

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
        self.activity_name.setValue(ColumnNumber)

    def set_CaseID_Column(self, ColumnNumber):
       # Sets the CaseID column if the column exists and all values in the column are non-empty
        with open(self.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            for row in csv_reader:
                if len(row) < ColumnNumber:
                    raise ValueError('Column number for Case IDs does not exist')
                if row[ColumnNumber-1] == '':
                    raise ValueError('One or more events do not have Case IDs')
        self.case_original_id.setValue(ColumnNumber)
    
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
        self.time_completed.setValue(ColumnNumber, Format)
