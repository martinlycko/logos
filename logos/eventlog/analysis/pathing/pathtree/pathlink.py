# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt
from typing import List, Any

# From other modules
from ....elements.case import Case


class PathLink(BaseModel):
    # A class to capturethe link between path nodes
    # Each link captures a source activity, target activity
    # and a collection of cases making this transition
    id: NonNegativeInt      # Generated, id of this link
    source: Any             # Source node of this link
    target: Any             # Target node, subsequent of souce node
    cases: List[Case] = []  # List of cases that follow this path
