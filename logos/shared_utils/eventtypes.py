from enum import Enum, auto


class EventType(Enum):
    # Types of events supported by the log
    # Should ultimately support all lifecycle event types in the XES standard
    # https://xes-standard.org/_media/xes/xesstandarddefinition-2.0.pdf
    complete = auto()
