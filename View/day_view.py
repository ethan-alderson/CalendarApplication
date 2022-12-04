
from Model.day import Day

class DayView:
    """ Represents the UI view of a given day """
    def __init__(self, day: Day) -> None:
        self.day = day

    def display(self):
        
        print("-" * 27)
        
        for startHour, event in self.day.events.values():
            print('|' + ':>25'.format(event.title) + f'{startHour}:{event.startMinute} -> {event.endHour}:{event.endMinute} |')

        print("-" * 27)