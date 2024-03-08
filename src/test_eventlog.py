from event_log import EventLog
from event_log_columns import EventLogCSV

if __name__ == "__main__":
    # Test initialising a new event log
    elog = EventLog()

    # Creating a new event log columns class
    csvlog = EventLogCSV("sample_data/running-example.csv")
    csvlog.event_original_id = 2
    csvlog.event_attributes = 6
    csvlog.start_time = 0
    csvlog.finish_time = 3
    csvlog.activity_name = 4
    csvlog.case_original_id = 1
    csvlog.case_attributes = 0
    csvlog.resource_name = 5
    csvlog.datetime_format = "%d-%m-%Y:%H.%M"
    
    # Test importing an working event log
    elog.add_events_from_CSV(csvlog)
    assert elog.events.count == 42
    assert elog.cases.count == 6
    assert elog.activities.count == 8
    assert elog.resources.count == 6

    # To be converted into a proper test - may not always be returned in same order, sample cases by ID
    # case=elog.cases.case_list[1].case_details()
    # print(case["path"][0].time_end)
    # print(case["path"][1].time_end)
    # print(case["path"][2].time_end)
    # print(case["path"][3].time_end)
    # print(case["path"][4].time_end)

    # Convert this into a test - should be 9 days 33 mins for case with internal ID 1
    # print(elog.cases.case_list[1].turnaround_time())

    # Tests the print function of the case class
    # print(elog.cases.case_list[1])

    # Print turnarount times by case number  
    # for caseID, turnaroundtime in elog.cases.turnaround_times().items():
    #     print(caseID, turnaroundtime)

    # Test turnaround stats
    # print(elog.cases.case_with_min_turnaround_time())
    # print(elog.cases.case_with_max_turnaround_time())
    # print(elog.cases.avg_turnaround_time())