# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt
from typing import List, Any

# From other modules
from ..elements.case import Case
from ..elements.activity import Activity


class Path(BaseModel):
    # A class to capture a single oath
    id: NonNegativeInt               # Generated, position in cases
    activities: List[Activity] = []  # List of activities in order for path
    cases: List[Case] = []           # List of cases that follow this path
