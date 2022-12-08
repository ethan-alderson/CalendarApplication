
from datetime import time

class Event:
    
    # events will be determined either a meeting or a task, then the title will be given, then description, then date, then time of day
    def __init__(self, title, description, startHour, startMinute, endHour, endMinute):
        
        if len(title) > 25:
            raise ValueError("Title must be 25 characters or less.")        
        
        self.title = title
        self.description = description
        self.startTime = time(startHour, startMinute, 0)
        self.endTime = time(endHour, endMinute, 0)


