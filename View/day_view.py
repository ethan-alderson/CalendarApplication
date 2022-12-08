
from Model.day import Day

class DayView:
    """ Represents the UI view of a given day """
    def __init__(self, day: Day) -> None:
        self.day = day

    def display(self):
        
        print("-" * 27)
        
        for event in self.day.events:
            print('|' + ':>25'.format(event.title) + f'{event.startTime.hour}:{event.startTime.minute} -> {event.endTime.hour}:{event.endTime.minute} |')

        print("-" * 27)