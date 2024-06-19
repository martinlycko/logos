# For type safety and code quality
from pydantic import BaseModel
from typing import List, Any

# From other modules
from ....elements.activity import Activity
from ....elements.case import Case


class PathNode(BaseModel):
    # A class to capture a node in a tree structure forming process paths
    # Each path node reflects an activity and points and subsequent activities
    # Also captured the cases that follow from this node to subsequent nodes
    children: List[Any] = []    # List of subsequent nodes/activities
    activity: Activity          # Activity of this node
    cases: List[Case] = []     # List of cases going through this node

    def __str__(self, level=0):
        ret = "- "*(level-1)+repr(self.activity.name)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
