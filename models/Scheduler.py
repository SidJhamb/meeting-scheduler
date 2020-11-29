from models.Employee import Employee
from models.MeetingRoom import MeetingRoom
from models.TimeInterval import TimeInterval
from models.Meeting import Meeting
from datetime import datetime, timedelta


class Scheduler:
    employees = []
    meetingRooms = []
    meetingIds = set([])

    def __init__(self):
        self.meetings = {}

    @staticmethod
    def init_meeting_scheduler(num_employees, num_meeting_rooms):
        for i in range(1, num_employees+1):
            Scheduler.employees.append(Employee(i))

        for i in range(1, num_meeting_rooms+1):
            Scheduler.meetingRooms.append(MeetingRoom(i))

        for i in range(1, 10000):
            Scheduler.meetingIds.add(i)


    def is_valid_request(self, employeeID, requestedInterval):
        if employeeID in self.meetings:
            for meeting in self.meetings[employeeID]:
                if requestedInterval == meeting.TimeInterval:
                    print("Error : You have exceeded the max limit of bookings at a time'")
                    return False

        if (requestedInterval.startTime - datetime.now()).days > 30:
            print("Error : Cannot book beyond 1 month from today")
            return False

        if (requestedInterval.endTime - requestedInterval.startTime).days > 3 / 24:
            print("Error : Cannot book a meeting of more than 3 hrs duration")
            return False

        return True

    def _has_conflict(self, employee_meetings, new_meeting):
        booked_intervals = []

        for meeting in employee_meetings:
            booked_intervals.append(TimeInterval(meeting.TimeInterval.startTime, meeting.TimeInterval.endTime))

        if len(booked_intervals) == 0 or (new_meeting.TimeInterval.endTime < booked_intervals[0].startTime):
            return False

        i = 0

        while i < (len(booked_intervals) - 1):
            prev = booked_intervals[i]
            next = booked_intervals[i + 1]

            if new_meeting.TimeInterval.startTime > prev.endTime and new_meeting.TimeInterval.endTime < next.startTime:
                return False
            i = i + 1

        if new_meeting.TimeInterval.startTime > booked_intervals[i].endTime:
            return False

        return True

    def _update_meetings(self, room, employeeID, new_meeting):
        if(employeeID not in self.meetings):
            self.meetings[employeeID] = []
            if not self._has_conflict(self.meetings[employeeID], new_meeting):
                self.meetings[employeeID].append(new_meeting)
                room.bookedMeetings.append(new_meeting)
                return True
            else:
                print("Error : You have a scheduled meeting which is conflicting.")
        else:
            if len(self.meetings[employeeID]) < 2:
                if not self._has_conflict(self.meetings[employeeID], new_meeting):
                    self.meetings[employeeID].append(new_meeting)
                    room.bookedMeetings.append(new_meeting)
                    return True
                else:
                    print("Error : Conflict.")
            else:
                print("Error : You are already the organizer of two scheduled meetings.")
                return False
            

    def schedule_meeting(self, employeeID, requestedInterval):
        if not self.is_valid_request(employeeID, requestedInterval):
            return

        for room in Scheduler.meetingRooms:
            booked_intervals = []

            for meeting in room.bookedMeetings:
                booked_intervals.append(TimeInterval(meeting.TimeInterval.startTime, meeting.TimeInterval.endTime))

            if len(booked_intervals) == 0 or (requestedInterval.endTime < booked_intervals[0].startTime):
                new_meeting = Meeting(Scheduler.meetingIds.pop(), requestedInterval, employeeID)
                if not self._update_meetings(room, employeeID, new_meeting):
                    return
                print("Meeting scheduled. Room ID : {}, Meeting ID : {}".format(room.meetingRoomID,
                                                                                new_meeting.meetingId))
                return

            i = 0

            while i < (len(booked_intervals) - 1):
                prev = booked_intervals[i]
                next = booked_intervals[i+1]

                if requestedInterval.startTime > prev.endTime and requestedInterval.endTime < next.startTime:
                    new_meeting = Meeting(Scheduler.meetingIds.pop(), requestedInterval, employeeID)
                    if not self._update_meetings(room, employeeID, new_meeting):
                        return
                    print("Meeting scheduled. Room ID : {}, Meeting ID : {}".format(room.meetingRoomID,
                                                                                    new_meeting.meetingId))
                    return
                i = i + 1

            if requestedInterval.startTime > booked_intervals[i].endTime:
                new_meeting = Meeting(Scheduler.meetingIds.pop(), requestedInterval, employeeID)
                if not self._update_meetings(room, employeeID, new_meeting):
                    return
                print("Meeting scheduled. Room ID : {}, Meeting ID : {}".format(room.meetingRoomID,
                                                                                new_meeting.meetingId))
                return

        print("Error : All rooms busy for the given time interval.")

    def cancel_meeting(self, employeeID, meetingID):
        if employeeID not in self.meetings:
            print("Error : The meeting is not booked by this employee.")
            return

        flag = True
        for meeting in self.meetings[employeeID]:
            if meeting.meetingId == meetingID:
                self.meetings[employeeID].remove(meeting)
                flag = False

        if flag:
            print("Error : You are not the organizer of this meeting.")
            return

        #self.meetings[employeeID] = list(filter(lambda m: m.meetingId != meetingID, self.meetings[employeeID]))

        print("Meeting is cancelled.")





            



