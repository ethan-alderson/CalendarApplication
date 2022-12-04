
from Model.day import Day

class DayView:
    """ Represents the UI view of a given day """
    def __init__(self, day: Day) -> None:
        self.day = day

    def display(self):

        for startHour, event in self.day.events.values():
            print("-" * 27)
            print('|' + ':>25'.format(event.title) + f'{startHour}:{event.startMinute} -> {event.endHour}:{event.endMinute} |')
