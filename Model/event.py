
from datetime import time

class Event:
    """ represents an event
    """

    def __init__(self, title, description, startHour, startMinute, endHour, endMinute):

        if len(title) > 19:
            raise ValueError('Title must be 19 characters or less.')        
        
        self.title = title
        self.description = description
        self.startTime = time(startHour, startMinute, 0)
        self.endTime = time(endHour, endMinute, 0)


    
