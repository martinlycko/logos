# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt
from typing import List

# From other modules
from ....elements.case import Case
from ....elements.activity import Activity


class PathLink(BaseModel):
    # A class to capturethe link between path nodes
    # Each link captures a source activity, target activity
    # and a collection of cases making this transition
    id: NonNegativeInt      # Generated, id of this link
    source: Activity        # Source activity of this link
    target: Activity        # Target activity, subsequent of source activity
    cases: List[Case] = []  # List of cases that follow this path
