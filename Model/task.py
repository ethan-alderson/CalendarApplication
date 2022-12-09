
from event import Event

# may need to rework the priority system, !!! or number system?
class Task(Event):
    def __init__(self, title, description, startHour, startMinute, endHour, endMinute, priority):
        super().__init__(title, description, startHour, startMinute, endHour, endMinute)

        if (priority != 1 and priority != 2 and priority != 3):
            raise TypeError("Invalid input for priority.")
        
        self.priority = priority
