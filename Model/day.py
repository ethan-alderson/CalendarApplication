from .event import Event
from datetime import date

class Day:
    def __init__(self, year, month, day):

        # keys will be start hours
        self.events = []
        self.date = date(year, month, day)

    # Adds an event to this day
    def addEvent(self, newEvent: Event):
        
        for event in self.events:
            if newEvent.startTime.hour > event.startTime.hour and newEvent.startTime.hour < event.endTime.hour:
                raise ValueError("Cannot add an event with conflicting event times.")

        else:
            self.events.append(newEvent)


# could do events with a dictionary with time as the key

