
from Model.day import Day
from Model.month import Month

class WeekView:
    """ Represents the GUI view of a given week"""
    def __init__(self, days) -> None:
        self.days = days

    def display(self):
        
        longestDay = self.days[0]
        
        # get the longest day
        for day in self.days:
            if len(day.events) > len(longestDay.events):
                longestDay = day    
        
        for day in self.days:
            print("-" * 40, end='')
        print("\r")
                  
        for day in self.days:
            print("| " + str(day.date) + " " * 27 + "|", end='') 
        print("\r")
        
        
        for day in self.days:
            print("-" * 40, end='')
            
            
        for i in range(len(longestDay.events)):
            for day in self.days:
                if len(day.events) < i:
                    lineString = f'| {day.events[i].title} : {str(day.events[i].startTime)[:-3]} -> {str(day.events[i].endTime)[:-3]}' + " " * (39 - len(lineString)) + "|"
                else:
                    lineString = " " * 39 + "|"
                    
                print(lineString, end="")
        
        
        # for event in self.day.events:
        #     lineString = f'| {event.title} : {str(event.startTime)[:-3]} -> {str(event.endTime)[:-3]}'
        #     print(lineString + " " * (45 - len(lineString)) + "|")

        # print("-" * 46)
        
        
    def handle_week_options(self, parentMonth: Month):
        print(f'Week from {parentMonth.name}')
        print(f'a) View Day')
        print(f'b) Return to {parentMonth.name}.')