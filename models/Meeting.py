import models.TimeInterval

class Meeting:
    def __init__(self, meetingId, TimeInterval, organizerId):
        self.meetingId = meetingId
        self.TimeInterval = TimeInterval
        self.organizerId = organizerId
