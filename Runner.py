from models.Scheduler import Scheduler
from models.TimeInterval import TimeInterval
from datetime import date, datetime, timedelta

meetingScheduler = Scheduler()

# Scheduler.init_meeting_scheduler(2, 1)
#
# start = datetime.now()
# end = start + timedelta(hours=3)
# start1 = start + timedelta(hours = 4)
# end1 = start + timedelta(hours = 6)
# start2 = start + timedelta(hours = 8)
# end2 = start + timedelta(hours = 10)
#
#
# print("1st")
# meetingScheduler.schedule_meeting(2, TimeInterval(start, end))
# print("2nd")
# result = meetingScheduler.schedule_meeting(2, TimeInterval(start1, end1))
# print("3rd")
# result = meetingScheduler.schedule_meeting(2, TimeInterval(start2, end2))

#meetingScheduler.cancel_meeting(3, 1)

flag = False

while True:
    if not flag:
        print("Enter 1 to initialise the meeting scheduler")
    print("Enter 2 to schedule a meeting")
    print("Enter 3 to cancel a meeting")
    print("Enter 4 to quit")
    userChoice = (int(input()))
    if userChoice is 1:
        if flag:
            print("Meeting scheduler already initialised.")
            continue
        print("Enter the number of meeting rooms")
        num_meeting_rooms = int(input())
        print("Enter the number of employees")
        num_employees = int(input())
        Scheduler.init_meeting_scheduler(num_employees, num_meeting_rooms)
        print("Meeting Scheduler initialized successfully")
        flag = True
    elif userChoice is 2:
        print("Enter your employee ID")
        employee_id = int(input())
        print("Enter the Meeting Start Date and Time in YYYY-MM-DD HH:MM format")
        start_date_time_str = input()
        start_date_time_obj = datetime.strptime(start_date_time_str, '%Y-%m-%d %H:%M')
        print("Enter the Meeting End Date and Time in YYYY-MM-DD HH:MM format")
        end_date_time_str = input()
        end_date_time_obj = datetime.strptime(end_date_time_str, '%Y-%m-%d %H:%M')
        result = meetingScheduler.schedule_meeting(employee_id, TimeInterval(start_date_time_obj, end_date_time_obj))
    elif userChoice is 3:
        print("Enter your employee ID")
        employee_id = int(input())
        print("Enter the meeting ID")
        meeting_id = int(input())
        meetingScheduler.cancel_meeting(employee_id, meeting_id)
    else:
        quit()








