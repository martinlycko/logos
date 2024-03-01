import pytest
from event_log import EventLog

if __name__ == "__main__":
    elog = EventLog()
    elog.add_events_from_CSV("sample_data/running-example.csv", [])
    assert elog.events.count == 42
    assert elog.cases.count == 6
    assert elog.activities.count == 8
    assert elog.resources.count == 6