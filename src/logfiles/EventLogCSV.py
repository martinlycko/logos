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

    def __init__(self, filepath, delimiter, CaseID_Column, ActivityName_Column, CompletedTime_Column, CompletedTime_Format) -> None:
        # Sets all mandatory event log elements
        self.set_FilePath(filepath, delimiter)
        self.set_ActivityName_Column(ActivityName_Column)
        self.set_CaseID_Column(CaseID_Column)
        self.set_TimeCompleted_Column(CompletedTime_Column, CompletedTime_Format)

    def check_Column(self, ColumnNumber):
        with open(self.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            for row in csv_reader:
                if len(row) < ColumnNumber:
                    raise ValueError('Column number does not exist')
        return True

    def check_NonEmptyColumn(self, ColumnNumber):
        with open(self.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            for row in csv_reader:
                if len(row) < ColumnNumber:
                    raise ValueError('Column number does not exist')
                if row[ColumnNumber-1] == '':
                    raise ValueError('One or more cells are empty')
        return True

    def check_DateTimeColumn(self, ColumnNumber, Format):
        with open(self.filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            line = 1
            for row in csv_reader:
                if line > 1:
                    if len(row) < ColumnNumber:
                        raise ValueError('Column number does not exist')
                    if row[ColumnNumber-1] == '':
                        raise ValueError('One or more cells are empty')
                    try:
                        timestamp = datetime.strptime(row[ColumnNumber-1], Format)
                    except ValueError:
                        raise ValueError('Not all datetime values match the provided format. Issue found in line: ' + str(line))
                line = line + 1
        return True

    def check_ColumnNumber(self, ColumnNumber):
        # Checks that a provided column number in a positive integer
        if (isinstance(ColumnNumber, int) == False
        or ColumnNumber < 1):
            raise ValueError('Column number not a positive integer')
        else:
            return True

    def check_ColumnAvailable(self, ColumnNumber):
        # Creates a list of all columns already being used
        usedColumns = [0]
        if self.time_completed.isSet == True:
            usedColumns.append(self.time_completed.getValue())
        if self.activity_name.isSet == True:
            usedColumns.append(self.activity_name.getValue())
        if self.case_original_id.isSet == True:
            usedColumns.append(self.case_original_id.getValue())
        if self.event_original_id.isSet == True:
            usedColumns.append(self.event_original_id.getValue())
        if self.time_received.isSet == True:
            usedColumns.append( self.time_received.getValue())
        if self.time_ready.isSet == True:
            usedColumns.append(self.time_ready.getValue())
        if self.time_start.isSet == True:
            usedColumns.append(self.time_start.getValue())
        if self.time_stop.isSet == True:
            usedColumns.append(self.time_stop.getValue())
        if self.resource_name.isSet == True:
            usedColumns.append(self.resource_name.getValue())
        if self.case_attributes.isSet == True:
            if isinstance(self.case_attributes.getValue, list) == True:
                 usedColumns.extend(self.case_attributes.getValue)
            else:
                usedColumns.append(self.case_attributes.getValue)
        if self.event_attributes.isSet == True:
            if isinstance(self.event_attributes.getValue, list) == True:
                 usedColumns.extend(self.event_attributes.getValue)
            else:
                usedColumns.append(self.event_attributes.getValue)
        print(usedColumns)
        # Error if column already used
        if len(usedColumns) == 0:
            return True
        else:
            if (ColumnNumber in usedColumns):
                raise ValueError('Column already used')
            else:
                return True

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
        if (self.check_ColumnNumber(ColumnNumber) == True
        and self.check_ColumnAvailable(ColumnNumber) == True
        and self.check_NonEmptyColumn(ColumnNumber) == True):
            self.activity_name.setValue(ColumnNumber)

    def set_CaseID_Column(self, ColumnNumber):
       # Sets the CaseID column if the column exists and all values in the column are non-empty
        if (self.check_ColumnNumber(ColumnNumber) == True
        and self.check_ColumnAvailable(ColumnNumber) == True
        and self.check_NonEmptyColumn(ColumnNumber) == True):
            self.case_original_id.setValue(ColumnNumber)
    
    def set_TimeCompleted_Column(self, ColumnNumber, Format):
        # Sets the FinishTime column if the column exists and all values can be converted into datetime format
        if (self.check_ColumnNumber(ColumnNumber) == True
        and self.check_ColumnAvailable(ColumnNumber) == True
        and self.check_DateTimeColumn(ColumnNumber, Format) == True):
            self.time_completed.setValue(ColumnNumber, Format)

    def set_EventID_Column(self, ColumnNumber):
        # Sets the EventID column if the column exists and all values in the column are non-empty
        if (self.check_ColumnNumber(ColumnNumber) == True
        and self.check_ColumnAvailable(ColumnNumber) == True
        and self.check_NonEmptyColumn(ColumnNumber) == True):
            self.event_original_id.setValue(ColumnNumber)

    def set_TimeReceived_Column(self, ColumnNumber, Format):
        # Sets the TimeReceived column if the column exists and all values can be converted into datetime format
        if (self.check_ColumnNumber(ColumnNumber) == True
        and self.check_ColumnAvailable(ColumnNumber) == True
        and self.check_DateTimeColumn(ColumnNumber, Format) == True):
            self.time_received.setValue(ColumnNumber, Format)

    def set_TimeReady_Column(self, ColumnNumber, Format):
        # Sets the TimeReady column if the column exists and all values can be converted into datetime format
        if (self.check_ColumnNumber(ColumnNumber) == True
        and self.check_ColumnAvailable(ColumnNumber) == True
        and self.check_DateTimeColumn(ColumnNumber, Format) == True):
            self.time_ready.setValue(ColumnNumber, Format)

    def set_TimeStart_Column(self, ColumnNumber, Format):
        # Sets the TimeStart column if the column exists and all values can be converted into datetime format
        if (self.check_ColumnNumber(ColumnNumber) == True
        and self.check_ColumnAvailable(ColumnNumber) == True
        and self.check_DateTimeColumn(ColumnNumber, Format) == True):
            self.time_start.setValue(ColumnNumber, Format)

    def set_TimeStop_Column(self, ColumnNumber, Format):
        # Sets the TimeStop column if the column exists and all values can be converted into datetime format
        if (self.check_ColumnNumber(ColumnNumber) == True
        and self.check_ColumnAvailable(ColumnNumber) == True
        and self.check_DateTimeColumn(ColumnNumber, Format) == True):
            self.time_stop.setValue(ColumnNumber, Format)

    def set_ResourceName_Column(self, ColumnNumber):
        # Sets the ResourceName column if the column exists
        if (self.check_ColumnNumber(ColumnNumber) == True
        and self.check_ColumnAvailable(ColumnNumber) == True
        and self.check_Column(ColumnNumber) == True):
            self.resource_name.setValue(ColumnNumber)

    def set_CaseAttributes_Column(self, ColumnNumbers):
        # Sets the ResourceName columns as a list if multiple values are provided as a list
        if isinstance(ColumnNumbers, list) == True:
            for i in ColumnNumbers:
                self.check_ColumnNumber(i)
                self.check_ColumnAvailable(i)
                self.check_Column(i)
            self.case_attributes.setValue(ColumnNumbers)
        # Sets the ResourceName columns as a scalar value if provided as scalar
        else:
            if (self.check_ColumnNumber(ColumnNumbers) == True
            and self.check_ColumnAvailable(ColumnNumbers) == True
            and self.check_Column(ColumnNumbers) == True):
                self.case_attributes.setValue(ColumnNumbers)

    def set_EventAttributes_Column(self, ColumnNumbers):
        # Sets the ResourceName columns as a list if multiple values are provided as a list
        if isinstance(ColumnNumbers, list) == True:
            for i in ColumnNumbers:
                self.check_ColumnNumber(i)
                self.check_ColumnAvailable(i)
                self.check_Column(i)
            self.event_attributes.setValue(ColumnNumbers)
        # Sets the ResourceName columns as a scalar value if provided as scalar
        else:
            if (self.check_ColumnNumber(ColumnNumbers) == True
            and self.check_ColumnAvailable(ColumnNumbers) == True
            and self.check_Column(ColumnNumbers) == True):
                self.event_attributes.setValue(ColumnNumbers)
