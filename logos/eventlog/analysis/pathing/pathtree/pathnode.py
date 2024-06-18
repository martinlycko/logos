# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt
from typing import List

# From other modules
from ....elements.activity import Activity
from .pathlink import PathLink


class PathNode(BaseModel):
    # A class to capture a node in a tree structure forming process paths
    # Each path node reflects an activity and points and subsequent activities
    # Also captured the cases that follow from this node to subsequent nodes
    id: NonNegativeInt                  # Generated, id of this node
    activity: Activity = []             # Activity of this node
    subsequents: List[PathLink] = []    # List of subsequent links
