# For type safety and code quality
from typing import List
from pydantic import BaseModel, FilePath, PositiveInt
from enum import Enum


class Delimeter(Enum):
    # Delimiter types supported in the CSV file
    Semicolon = ";"
    Comma = ","


class DateTimeColumn(BaseModel):
    # Composition of column numberand format
    Column: PositiveInt
    Format: str


class EventLogCSV(BaseModel):
    # CSV file details
    filepath: FilePath
    delimiter: Delimeter

    # Mandatory columns of the event log
    time_completed: DateTimeColumn
    id_activity: PositiveInt
    id_case: PositiveInt

    # Optional, single-column elements of the event log
    id_event: PositiveInt | None = None
    time_received: DateTimeColumn | None = None
    time_ready: DateTimeColumn | None = None
    time_start: DateTimeColumn | None = None
    time_stop: DateTimeColumn | None = None
    id_resource: PositiveInt | None = None

    # Optional, single- or multi-column elements of the event log
    attributes_case: List[PositiveInt] | None = None
    attributes_event: List[PositiveInt] | None = None
