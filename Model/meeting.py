
from .event import Event

class Meeting(Event):
    """ Represents a meeting, subclass of Event
    """
    def __init__(self, title, description, startHour, startMinute, endHour, endMinute, recipient):
        super().__init__(title, description, startHour, startMinute, endHour, endMinute)
        self.recipient = recipient
