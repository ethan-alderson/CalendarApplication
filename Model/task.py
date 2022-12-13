
from .event import Event

# Represents a task
class Task(Event):
    """ Represents a task, subclass of Event
    """
    def __init__(self, title, description, startHour, startMinute, endHour, endMinute, priority):
        super().__init__(title, description, startHour, startMinute, endHour, endMinute)

        if (priority != 1 and priority != 2 and priority != 3):
            raise TypeError('Invalid input for priority.')
        
        self.priority = priority
