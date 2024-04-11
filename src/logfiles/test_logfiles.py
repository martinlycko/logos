from EventLogCSV import EventLogCSV

def test_running_example():
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

if __name__ == "__main__":
    test_running_example()

    # Tests to create:
    # Incorrect filepaths
    # Incorrect file extensions
    # Column number is not a number
    # Column number does not exist in file
    # Column includes empty values