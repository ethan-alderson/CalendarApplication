
from Model.day import Day
from Model.month import Month
# from View.month_view import MonthView
from Model.meeting import Meeting
from Model.task import Task

class DayView:
    """ Represents the UI view of a given day """
    def __init__(self, day: Day, parentMonth: Month) -> None:
        self.day = day

    def display(self):
        
        print("-" * 40)
        print("| " + str(self.day.date) + " " * 27 + "|") 
        print("-" * 460)
        
        for event in self.day.events:
            lineString = f'| {event.title} : {str(event.startTime)[:-3]} -> {str(event.endTime)[:-3]}'
            print(lineString + " " * (39 - len(lineString)) + "|")

        print("-" * 40)
        
    def handle_day_options(self, parentMonth: Month):

        viewingDay = True
        
        while (viewingDay):
                
            print(f'Date: {self.day.date}')
            print(f'a) Add Event')
            print(f'b) Remove Event')
            print(f'c) View {parentMonth.name}.')
        
            option = input("Select an option (a, b, c): ")
        
            if option != 'a' and option != 'b' and option != 'c':
                print("Invalid option, select again.")
                continue
            
            if option == 'a':
                self.addEventHandler()
                
            if option == 'b':
                self.removeEventHandler()
            
            if option == 'c':
                viewingDay = False
                
            # monthviewer = MonthView(parentMonth)
            # monthviewer.display()
            # monthviewer.handle_month_options()
        
        
        
    def addEventHandler(self):
        
        suboption = ''
        
        while suboption != 'a' and suboption != 'b' and suboption != 'c':
            print('a) Meeting')
            print('b) Task')
            print('c) Exit.')
            suboption = input(f'What type of event would you like to add? ')
        
        addingEvent = True
        
        while (addingEvent):
            
            # collect data
            title = input('Enter the meeting title: ')
            description = input('Enter the meeting description: ')
            startTimeInput = input('Enter the meeting start time (No need for AM or PM, format in hh:mm): ')
            startAMOrPM = input('PM? (y/n): ')
            endTimeInput = input('Enter the meeting end time in military (hh:mm): ')
            endAMorPM = input('PM? (y/n): ')
            
            
            if suboption == 'a':
                recipient = input('Enter the meeting recipient: ')
                
            if suboption == 'b':
                priority = input('Enter task priority: ')
            
            # parse startTime
            startHour, startMinute = startTimeInput.split(":")
            
            startHour = int(startHour)
            startMinute = int(startMinute)
            
            if (startAMOrPM == 'y'):
                startHour += 12
            
            # parse endTime
            endHour, endMinute = endTimeInput.split(":")
            
            endHour = int(endHour)
            endMinute = int(endMinute)
            
            if (endAMorPM == 'y'):
                endHour += 12
            
            if suboption == 'a':
                newEvent = Meeting(title, description, startHour, startMinute, endHour, endMinute, recipient)
                
            if suboption == 'b':
                newEvent = Task(title, description, startHour, startMinute, endHour, endMinute, priority)
            
            self.day.addEvent(newEvent)         
            
        if suboption == 'c':
            self.handle_day_options()

    def removeEventHandler(self):
        suboption = input(f'Name the event you\'d like to remove: ')
        
        initialLength = len(self.day.events)
        
        self.day.events = [event for event in self.day.events if event.title != suboption]
        
        finalLength = len(self.day.events)
        
        if initialLength == finalLength:
            print("The event you named was not found on this day.")