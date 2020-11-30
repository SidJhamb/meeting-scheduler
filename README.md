# Meetings Scheduler

## Requirements
* Python 3

## Quick Start
Following are the steps to run the application.

1. Start the Python Virtual Environment

```
python3 -m venv env
source env/bin/activate
```

2. Run the application

```
python Runner.py
```

On running, the user would see the following options at first.

```
Enter 1 to initialise the meeting scheduler
Enter 2 to schedule a meeting
Enter 3 to cancel a meeting
Enter 4 to quit
```

## How it works

1. Initialising the meeting scheduler.
   Please note :
   - Employee IDs are assigned by default from (1 - Number of employees entered)
   - Meeting Room IDs are assigned by default from ( 1 - Number of meeting rooms entered)

```
1
Enter the number of meeting rooms
2
Enter the number of employees
2
Meeting Scheduler initialized successfully
```

2. Scheduling a meeting

```
2
Enter your employee ID
1
Enter the Meeting Start Date and Time in YYYY-MM-DD HH:MM format
2020-12-20 00:00
Enter the Meeting End Date and Time in YYYY-MM-DD HH:MM format
2020-12-20 00:15
Meeting scheduled. Room ID : 1, Meeting ID : 1
```

3. Cancel a meeting

```
3
Enter your employee ID
1
Enter the meeting ID
1
Meeting is cancelled.
```

4. Quit the scheduler

```
4
```

## Constraint Handling

The scheduler handles all the constraints mentioned in the problem statement, and the success or error messages received are self explanatory.
