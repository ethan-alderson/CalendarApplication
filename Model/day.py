from event import Event
from datetime import date

class Day:
    def __init__(self, year, month, day):

        # keys will be start hours
        self.events = {}
        self.date = date(year, month, day)

    # Adds an event to this day
    def addEvent(self, newEvent):
        
        for k, v in self.events:
            if newEvent.startHour > k and newEvent.endHour < v.endHour:
                raise ValueError("Cannot add an event with conflicting event times.")

        else:
            self.events[newEvent.startHour] = newEvent


# could do events with a dictionary with time as the key