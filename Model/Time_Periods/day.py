from Model.event import Event
from datetime import date

class Day:
    def __init__(self, date):

        if (type(date) != date):
            raise TypeError("Invalid input for addEvent.")

        self.tasks = []
        self.date = date


    def addEvent(self, newEvent):
        
        if (type(newEvent) != Event):
            raise TypeError("Invalid input for addEvent.")

        self.tasks.append(newEvent)
