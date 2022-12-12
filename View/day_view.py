
from Model.day import Day
from Model.month import Month
# from View.month_view import MonthView
from Model import Meeting
from Model.task import Task
import re

class DayView:
    """ Represents the UI view of a given day """
    def __init__(self, day: Day) -> None:
        self.day = day

    def display(self):
        
        print('-' * 40)
        print('| ' + str(self.day.date) + ' ' * 27 + '|') 
        print('-' * 40)
        
        for event in self.day.events:
            lineString = f'| {event.title} : {str(event.startTime)[:-3]} -> {str(event.endTime)[:-3]}'
            print(lineString + ' ' * (39 - len(lineString)) + '|')

        print('-' * 40)
    
    
    def handle_day_options(self, parentMonth: Month):

        viewingDay = True
        
        while (viewingDay):
                
            self.display()
            
            print(f'Date: {self.day.date}')
            print(f'a) Add Event')
            print(f'b) Remove Event')
            print(f'c) View {parentMonth.name}.')
        
            option = input('Select an option (a, b, c): ')
        
            if option != 'a' and option != 'b' and option != 'c':
                print('Invalid option, select again.')
                continue
            
            if option == 'a':
                self.addEventHandler()
                
            if option == 'b':
                self.removeEventHandler()
            
            if option == 'c':
                viewingDay = False
        
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
            title = input('Enter event title: ')
            description = input('Enter the event description: ')
            
            # use regex to check time input format
            gettingStart = True
            while gettingStart:

                startTimeInput = input('Enter the event start time (No need for AM or PM, format in hh:mm): ')
                
                test1 = re.match('^[0-9]{2}:[0-9]{2}$', startTimeInput)
                test2 = re.match('^[1-9]{1}:[0-9]{2}$', startTimeInput)

                if not test1 and not test2:
                    print('Time must be hh:mm or h:mm')
                    continue
                else:
                    startHour, startMinute = startTimeInput.split(':')
                    startHour = int(startHour)
                    startMinute = int(startMinute)
                
                if startHour > 12 or startHour < 1:
                    print('Hour must be between 1 and 12')
                elif startMinute > 59 or startMinute < 0:
                    print('Minute must be between 0 and 59')
                else:
                    gettingStart = False

            gettingPM = True
            while gettingPM:
                startAMOrPM = input('PM? (y/n): ')

                if startAMOrPM.lower() != 'y' and startAMOrPM.lower() != 'n':
                    print('Invalid input, try again.')
                else:
                    gettingPM = False

            # use regex to check time input format
            gettingEnd = True
            while gettingEnd:

                endTimeInput = input('Enter the event end time (No need for AM or PM, format in hh:mm): ')

                test1 = re.match('^[0-9]{2}:[0-9]{2}$', endTimeInput)
                test2 = re.match('^[1-9]{1}:[0-9]{2}$', endTimeInput)

                if not test1 and not test2:
                    print('Time must be hh:mm or h:mm')
                    continue
                else:
                    endHour, endMinute = endTimeInput.split(':') 
                    endHour = int(endHour)
                    endMinute = int(endMinute)

                if endHour > 12 or endHour < 1:
                    print('Hour must be between 1 and 12')
                elif endMinute > 59 or endMinute < 0:
                    print('Minute must be between 0 and 59')
                else:
                    gettingEnd = False

            gettingPM = True
            while gettingPM:
                endAMorPM = input('PM? (y/n): ')

                if endAMorPM.lower() != 'y' and endAMorPM.lower() != 'n':
                    print('Invalid input, try again.')
                else:
                    gettingPM = False
            
            if suboption == 'a':
                recipient = input('Enter the meeting recipient: ')
                
            if suboption == 'b':
                priority = int(input('Enter task priority: '))
            
            # parse startTime
            startHour, startMinute = startTimeInput.split(':')
            
            startHour = int(startHour)
            startMinute = int(startMinute)
            
            if (startAMOrPM == 'y'):
                startHour += 12
            
            # parse endTime
            endHour, endMinute = endTimeInput.split(':')
            
            endHour = int(endHour)
            endMinute = int(endMinute)
            
            if (endAMorPM == 'y'):
                endHour += 12
            
            if suboption == 'a':
                newEvent = Meeting(title, description, startHour, startMinute, endHour, endMinute, recipient)
                
            if suboption == 'b':
                newEvent = Task(title, description, startHour, startMinute, endHour, endMinute, priority)
            
            self.day.addEvent(newEvent)         
            addingEvent = False
             
        if suboption == 'c':
            self.handle_day_options()

    def removeEventHandler(self):
        
        suboption = input(f'Name the event you\'d like to remove: ')
        
        initialLength = len(self.day.events)
        
        self.day.events = [event for event in self.day.events if event.title != suboption]
        
        finalLength = len(self.day.events)
        
        if initialLength == finalLength:
            print('The event you named was not found on this day.')