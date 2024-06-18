# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt
from typing import List

# From other modules
from .pathnode import PathNode
from ....elements.case import Case


class PathTree(BaseModel):
    # Contains the top level path nodes
    # These are the start events of the process
    startEvents: List[PathNode] = []  # List of nodes starting

    def add_case(case) -> None:
        # Adds a new case to the pathtree
        
        # Reference to preceding node or none if first activity
        precedingNode = None

        for activity in case.path:
            # For the start event of this node / precedingNode == None
                # Check if the activity is already in the startEvents list
                    # If not,
                        # Create a new node
                        # Set nodes activity to current activity
                # Update precedingNode to the newly created / identified node

            # For all non-start event activities of the case / precedingNode <> None
                # Check if the activity is already in the precedingNode's subsequents targets
                    # If not
                        # Create a new node
                            # Set nodes activity to current activity
                        # Create a new link
                            # Set target to current activity 
                            # Set origin to precedingNode's acticity
                                # Targets / Origins have to be nodes too
                                # Not activities
                            # Add case to link's case list
                    # If it is
                        # Get relevant link
                        # Add case to link's case list
                # Update precedingNode to the new / identified node
                