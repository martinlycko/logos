from events import Events
from cases import Cases
from activities import Activities
from resources import Resources

class EventLog:
    # A class to capture the entire event log structure
    
    # Each event log contains a list of events, cases, activities, and resources
    events = Events()
    cases = Cases()
    activities = Activities()
    resources = Resources()

    def __init__(self) -> None:
        self.events = Events()
        self.cases = Cases()
        self.activities = Activities()
        self.resources = Resources()