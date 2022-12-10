from .event import Event
from datetime import date

class Day:
    def __init__(self, year, month, day):

        self.events = []
        self.date = date(year, month, day)


    def addEvent(self, newEvent: Event):
        """ adds an event to the day

        Args:
            newEvent (Event): the event to be added
        """
        
        self.events.append(newEvent)



