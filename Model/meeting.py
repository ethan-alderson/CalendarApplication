
from event import Event

class Meeting(Event):

    def __init__(self, title, description, startHour, startMinute, endHour, endMinute, recipient):
        super().__init__(title, description, startHour, startMinute, endHour, endMinute)
        self.recipient = recipient
