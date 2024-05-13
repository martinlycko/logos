# For type safety and code quality
from typing import Optional, List
from pydantic import BaseModel, FilePath
from enum import Enum


class Delimeter(Enum):
    Semicolon = ";"
    Comma = ","


class DateTimeColumn(BaseModel):
    Column: int
    Format: str


class EventLogCSV(BaseModel):
    # CSV file details
    filepath: FilePath
    delimiter: Delimeter

    # Mandatory columns of the event log
    time_completed = DateTimeColumn
    activity_name = str
    case_original_id = str

    # Optional, single-column elements of the event log
    event_original_id: Optional[str] = None
    time_received: Optional[DateTimeColumn] = None
    time_ready: Optional[DateTimeColumn] = None
    time_start: Optional[DateTimeColumn] = None
    time_stop: Optional[DateTimeColumn] = None
    resource_name: Optional[str] = None

    # Optional, single- or multi-column elements of the event log
    case_attributes: Optional[List[int]] = None
    event_attributes: Optional[List[int]] = None
