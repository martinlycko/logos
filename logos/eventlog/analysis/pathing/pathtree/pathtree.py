# For type safety and code quality
from pydantic import BaseModel
from typing import List

# From other modules
from .pathnode import PathNode
from .pathlink import PathLink


class PathTree(BaseModel):
    # Contains the top level path nodes
    # These are the start events of the process
    startEvents: List[PathNode] = []  # List of nodes starting

    def add_case(self, case) -> None:
        # Adds a new case to the pathtree

        # Reference to preceding node or none if first activity
        precedingNode = None

        for activity in case.path:
            # For the start event of this node
            if precedingNode is None:
                inList = False
                # Check each item in the startEvent list
                for node in self.startEvents:
                    if node.activity == activity:
                        inList = True
                        precedingNode = node
                if inList is False:
                    # Create a new node
                    newNode = PathNode(
                         activity=activity
                         )
                    self.startEvents.append(newNode)
                    # Update precedingNode to the newly created
                    precedingNode = newNode
            # For all non-start event activities of the case
            else:
                inList = False
                # Check each item in the startEvent list
                for link in precedingNode.subsequents:
                    if link.target.activity == activity:
                        inList = True
                        link.cases.append(case)
                        precedingNode = link.target
                if inList is False:
                    # Create a new node
                    newNode = PathNode(
                         activity=activity
                         )
                    # Create a new link
                    newLink = PathLink(
                        source=precedingNode,
                        target=newNode
                        )
                    # Connect case, node, and link
                    newNode.subsequents.append(newLink)
                    newLink.cases.append(case)
                    # Update precedingNode to the newly created
                    precedingNode = newNode
