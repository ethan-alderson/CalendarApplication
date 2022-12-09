
from Model.month import Month
from View.day_view import DayView
# from View.month_view import MonthView

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
            print('-' * 40, end='')
        print('\r')
                  
        for day in self.days:
            print('| ' + str(day.date) + ' ' * 27 + '|', end='') 
        print('\r')
        
        
        for day in self.days:
            print('-' * 40, end='')
            
            
        for i in range(len(longestDay.events)):
            for day in self.days:
                if len(day.events) < i:
                    lineString = f'| {day.events[i].title} : {str(day.events[i].startTime)[:-3]} -> {str(day.events[i].endTime)[:-3]}' + ' ' * (39 - len(lineString)) + '|'
                else:
                    lineString = ' ' * 39 + '|'
                    
                print(lineString, end='')
        
        
        # for event in self.day.events:
        #     lineString = f'| {event.title} : {str(event.startTime)[:-3]} -> {str(event.endTime)[:-3]}'
        #     print(lineString + ' ' * (45 - len(lineString)) + '|')

        # print('-' * 46)
        
        
    def handle_week_options(self, parentMonth: Month):
        
        viewingWeek = True
        
        while (viewingWeek):
                
            print(f'Week from {parentMonth.name}')
            print(f'a) View Day')
            print(f'b) Return to {parentMonth.name}.')
        
            option = input('Select an option (a, b): ')
        
            if option != 'a' and option != 'b':
                print('Invalid option, select again.')
                continue
            
            if option == 'a':
                
                gettingPosition = True
                while (gettingPosition):
                    position = int(input(f'Which day would you like to view (enter the position in the week, starting at 1): '))
                
                if position < 0:
                    print("Position cannot be negative.")
                    
                if position > len(self.days):
                    print("Position out of bounds.")
                
                dayViewer = DayView(self.days[position - 1])
                dayViewer.display()
                dayViewer.handle_day_options()
                
            if option == 'b':
                viewingWeek = False
                # monthViewer = MonthView(parentMonth)
                # monthViewer.display()
                # monthViewer.handle_month_options()
                               
            
            
        