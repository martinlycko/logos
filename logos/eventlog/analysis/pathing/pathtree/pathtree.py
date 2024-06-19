# For type safety and code quality
from pydantic import BaseModel
from typing import List

# From other modules
from .pathnode import PathNode


class PathTree(BaseModel):
    # Contains the top level path nodes
    # These are the start events of the process
    children: List[PathNode] = []  # List of nodes starting

    def add_case(self, case) -> None:
        # Adds a new case to the pathtree

        # Reference to preceding node or none if first activity
        precedingNode = None

        for activity in case.path:            
            # For the start event of this node
            if precedingNode is None:
                inList = False
                # Check each item in the startEvent list
                for node in self.children:
                    if node.activity == activity:
                        inList = True
                        precedingNode = node
                if inList is False:
                    # Create a new node
                    newNode = PathNode(
                         activity=activity
                         )
                    newNode.cases.append(case)
                    self.children.append(newNode)
                    # Update precedingNode to the newly created
                    precedingNode = newNode
            # For all non-start event activities of the case
            else:
                inList = False
                # Check each item in the startEvent list
                for node in precedingNode.children:
                    if node.activity == activity:
                        inList = True
                        node.cases.append(case)
                        precedingNode = node
                if inList is False:
                    # Create a new node
                    newNode = PathNode(
                         activity=activity
                         )
                    newNode.cases.append(case)
                    precedingNode.children.append(newNode)
                    # Update precedingNode to the newly created
                    precedingNode = newNode

    def __str__(self, level=0):
        ret = ""
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
