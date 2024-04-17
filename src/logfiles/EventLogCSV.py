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
    
    # CSV file details
    filepath = ""
    delimiter = ""
    
    # Mandatory columns of the event log
    time_completed = DateColumnValueSet()
    activity_name = ColumnsSet()
    case_original_id = ColumnsSet()

    # Optional, single-column elements of the event log
    event_original_id = ColumnsSet()
    time_received = DateColumnValueSet()
    time_ready = DateColumnValueSet()
    time_start = DateColumnValueSet()
    time_stop = DateColumnValueSet()
    resource_name = ColumnsSet()

    # Optional, single- or multi-column elements of the event log
    case_attributes = ColumnsSet()
    event_attributes = ColumnsSet()

    # Sets all mandatory event log elements
    def __init__(self, filepath, delimiter, CaseID_Column, ActivityName_Column, CompletedTime_Column, CompletedTime_Format) -> None:
        self.set_FilePath(filepath, delimiter)
        self.set_ActivityName_Column(ActivityName_Column)
        self.set_CaseID_Column(CaseID_Column)
        self.set_TimeCompleted_Column(CompletedTime_Column, CompletedTime_Format)

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
    
    def set_TimeCompleted_Column(self, ColumnNumber, Format):
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

    def set_EventID_Column(self, ColumnNumber):
        # Sets the EventID column if the column exists and all values in the column are non-empty
        with open(self.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            for row in csv_reader:
                if len(row) < ColumnNumber:
                    raise ValueError('Column number for activities does not exist')
                if row[ColumnNumber-1] == '':
                    raise ValueError('One or more events do not have activity names')
        self.event_original_id.setValue(ColumnNumber)

    def set_TimeReceived_Column(self, ColumnNumber, Format):
        # Sets the TimeReceived column if the column exists and all values can be converted into datetime format
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
        self.time_received.setValue(ColumnNumber, Format)

    def set_TimeReady_Column(self, ColumnNumber, Format):
        # Sets the TimeReady column if the column exists and all values can be converted into datetime format
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
        self.time_ready.setValue(ColumnNumber, Format)

    def set_TimeStart_Column(self, ColumnNumber, Format):
        # Sets the TimeStart column if the column exists and all values can be converted into datetime format
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
        self.time_start.setValue(ColumnNumber, Format)

    def set_TimeStop_Column(self, ColumnNumber, Format):
        # Sets the TimeStop column if the column exists and all values can be converted into datetime format
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
        self.time_stop.setValue(ColumnNumber, Format)

    def set_ResourceName_Column(self, ColumnNumber):
        # Sets the ResourceName column if the column exists
        with open(self.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            for row in csv_reader:
                if len(row) < ColumnNumber:
                    raise ValueError('Column number for activities does not exist')
        self.resource_name.setValue(ColumnNumber)

    # def set_CaseAttributes
    # def set_EventAttributes