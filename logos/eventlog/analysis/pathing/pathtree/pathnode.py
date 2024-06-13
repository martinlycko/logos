# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt
from typing import List

# From other modules
from ....elements.case import Case
from ....elements.activity import Activity


class PathNode(BaseModel):
    # A class to capture a node in a tree structure forming process paths
    # Each path node reflects an activity and points and subsequent activities
    # Also captured the cases that follow from this node to subsequent nodes
    id: NonNegativeInt               # Generated, position in cases
    activities: List[Activity] = []  # List of activities in order for path
    cases: List[Case] = []           # List of cases that follow this path
