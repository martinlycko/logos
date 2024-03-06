from event_log import EventLog

if __name__ == "__main__":
    # Test initialising a new event log
    elog = EventLog()
    
    # Test importing an working event log
    elog.add_events_from_CSV("sample_data/running-example.csv", [], "%d-%m-%Y:%H.%M")
    assert elog.events.count == 42
    assert elog.cases.count == 6
    assert elog.activities.count == 8
    assert elog.resources.count == 6

    # To be converted into a proper test - may not always be returned in same order, sample cases by ID
    case=elog.cases.case_list[1].case_details()
    print(case["path"][0].time_end)
    print(case["path"][1].time_end)
    print(case["path"][2].time_end)
    print(case["path"][3].time_end)
    print(case["path"][4].time_end)

    # Convert this into a test - should be 9 days 33 mins for case with internal ID 1
    print(elog.cases.case_list[1].turnaround_time())