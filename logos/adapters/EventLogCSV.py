# For type safety and code quality
from typing import List
from pydantic import BaseModel, FilePath, PositiveInt
from enum import Enum

from ..shared_utils.eventtypes import EventType


class Delimeter(Enum):
    # Delimiter types supported in the CSV file
    Semicolon = ";"
    Comma = ","


class DateTimeColumn(BaseModel):
    # Composition of column number, format, and event type
    Column: PositiveInt
    Format: str
    Stage: EventType


class EventLogCSV(BaseModel):
    # CSV file details
    filepath: FilePath
    delimiter: Delimeter

    # Mandatory columns of the event log
    time: DateTimeColumn
    id_activity: PositiveInt
    id_case: PositiveInt

    # Optional, single-column elements of the event log
    id_event: PositiveInt | None = None
    id_resource: PositiveInt | None = None

    # Optional, single- or multi-column elements of the event log
    attributes_case: List[PositiveInt] | None = None
    attributes_event: List[PositiveInt] | None = None
