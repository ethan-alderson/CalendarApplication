
from datetime import time

class Event:
    
    # events will be determined either a meeting or a task, then the title will be given, then description, then date, then time of day
    def __init__(self, title, description, startHour, startMinute, endHour, endMinute):

        if (type(title) != str):
            raise TypeError("Invalid input for title.")

        if (type(description) != str):
            raise TypeError("Invalid input for description.")

            
        self.title = title
        self.description = description
        self.startTime = time(startHour, startMinute, 0)
        self.endTime = time(endHour, endMinute, 0)


