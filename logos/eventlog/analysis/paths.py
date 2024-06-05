# For type safety and code quality
from pydantic import BaseModel
from typing import List

# Reference to other event log classes
from .path import Path


class Paths(BaseModel):
    # A class to capture all paths
    pathList: List[Path] = []   # A list of paths

    def add_case(self, case) -> None:
        # Check if any of the existing paths match the case
        pathfound = False
        for path in self.pathList:
            if case.path == path.activities:
                # Add the case to the path's case list
                path.cases.append(case)
                pathfound = True
        # Create a new path
        if pathfound is False:
            new_path = Path(
                id=len(self.pathList),
            )
            for activity in case.path:
                new_path.activities.append(activity)
            new_path.cases.append(case)
        self.pathList.append(new_path)
