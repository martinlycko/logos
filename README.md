# logos
A work-in-process library to **analyse event logs** to determine process performance and analyse user bahviour

Currently planned initial features:
- Import a flat csv file of an event log (in progress)
- Transform the flat file into a custom data structure covering cases, events, resources, and activities (in progress)
- Summaries of the event log and individual cases, events, resources, and activities (in progress)
- Provide a timeseries of start events in total and for each start event
- Provide statistical measures of performance by activity and resource
- Illustrate the performance development statistics over time
- Determine the development of backlogs in the process in total and by resource
- Investigate how case attributes contribute to performance characteristics
- Identify the paths taken by different cases through the process

Methodologies used to create this library:
- Test- and behaviour driven development
- Python, with later options to rewrite in Rust with Python bindings