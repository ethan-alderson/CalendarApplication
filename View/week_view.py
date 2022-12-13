
import sys
import io

from Model.month import Month
from View.day_view import DayView


class WeekView:
    """Represents the GUI view of a given week"""
    def __init__(self, days) -> None:
        self.days = days

    def display(self):    
        """Displays the UI of the week to the user
        """
        for day in self.days:
            print('-' * 40, end='')
        print('\r')
                  
        for day in self.days:
            print('| ' + str(day.date) + ' ' * 27 + '|', end='')
        print('\r')
        
        
        for day in self.days:
            print('-' * 40, end='')
        
        print('\r')

        longestDay = self.days[0]
        
        # get the longest day
        for day in self.days:
            if len(day.events) > len(longestDay.events):
                longestDay = day

        for i in range(len(longestDay.events)):
            for day in self.days:
                if len(day.events) > i:
                    eventString = f'{day.events[i].title} : {str(day.events[i].startTime)[:-3]} -> {str(day.events[i].endTime)[:-3]}'
                    lineString = '| ' + eventString + ' ' * (37 - len(eventString)) + '|'
                else:
                    lineString = '|' + ' ' * 38 + '|'
                    
                print(lineString, end='')

            print('\r')

        for day in self.days:
            print('-' * 40, end='')
    
    @staticmethod
    def testDisplay(week):
        """test method, all it does is run display but reroute the print statement into a StringIO object. 
        It does this so that we can check the display output in our tests even though it only prints to the console.

        Args:
            week (List of days): The days to display

        Returns:
            String: The entire display in a single string
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        wv1 = WeekView(week)
        wv1.display()
        sys.stdout = sys.__stdout__

        return capturedOutput.getvalue()

    def handle_week_options(self, parentMonth: Month):
        """ Handles the user inputs for the current weekview

        Args:
            parentMonth (Month): The month that this week came from
        """
        viewingWeek = True
        
        while (viewingWeek):
            
            self.display()
            
            print('\r')               
            print(f'Week from {parentMonth.name}')
            print(f'a) View Day')
            print(f'b) Return to {parentMonth.name}.')
        
            option = input('Select an option (a, b): ')
        
            if option != 'a' and option != 'b':
                print('Invalid option, select again.')
                continue
            
            # transition to day
            if option == 'a':
                
                gettingPosition = True
                while (gettingPosition):
                    position = int(input(f'Which day would you like to view (enter the position in the week, starting at 1): '))
                
                    if position < 0:
                        print('Position cannot be negative.')
                    
                    elif position > len(self.days):
                        print('Position out of bounds.')
                
                    else:
                        gettingPosition = False
                
                dayViewer = DayView(self.days[position - 1])
                dayViewer.handle_day_options(parentMonth)

            # go back to the previous month view 
            if option == 'b':
                viewingWeek = False
                
                               
            
            
        