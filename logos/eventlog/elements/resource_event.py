# For type safety and code quality
from pydantic import BaseModel, NonNegativeInt


class Resource(BaseModel):
    # A class to capture a single case
    id: NonNegativeInt          # Generated, position in resources
    name: str                   # Imported from the event log
