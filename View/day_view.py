
from model.day import Day

class DayView:
    """ Represents the UI view of a given day """
    def __init__(self, day: Day) -> None:
        self.day = day

    def display(self):
        
        print("-" * 46)
        print("| " + str(self.day.date) + " " * 33 + "|") 
        print("-" * 46)
        
        for event in self.day.events:
            lineString = f'| {event.title} : {str(event.startTime)[:-3]} -> {str(event.endTime)[:-3]}'
            print(lineString + " " * (45 - len(lineString)) + "|")

        print("-" * 46)