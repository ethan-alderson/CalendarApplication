from .event import Event
from datetime import date, timedelta

class Day:
    def __init__(self, year, month, day):

        self.events = []
        self.date = date(year, month, day)


    def addEvent(self, newEvent: Event):
        """ adds an event to the day

        Args:
            newEvent (Event): the event to be added
        """
        
        added = False

        if len(self.events) == 0:
            self.events.append(newEvent)
            added = True

        else:
            # for each event in the range

            low = 0
            high = None

            if low < 0:
                raise ValueError('lo must be non-negative')
            if high is None:
                high = len(self.events)
            while low < high:
                middle = (low + high) // 2
                if newEvent.startTime.hour < self.events[middle].startTime.hour:
                    high = middle
                else:
                    low = middle + 1
            self.events.insert(low, newEvent)



