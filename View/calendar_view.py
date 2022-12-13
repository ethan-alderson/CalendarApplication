
import pickle

import sys
import io

from Model.calendar import Calendar
from View.year_view import YearView


class CalendarView:
    """represents the UI for the calendar
    """
    def __init__(self, calendar: Calendar) -> None:
        self.calendar = calendar
    
    def display(self):
        """Displays the initial method

        VOID
        """
        print(f'Welcome to your Calendar! This is a calendar of your events from {self.calendar.years[0].calendarYear} to {self.calendar.years[-1].calendarYear}!')
    
    @staticmethod
    def testDisplay(calendar: Calendar):
        """ test method, all it does is run display but reroute the print statement into a StringIO object. 
        It does this so that we can check the display output in our tests even though it only prints to the console.

        Args:
            calendar (Calendar): the calendar to test display

        Returns:
            String: The full displayed string of the calendar
        """
        printed = io.StringIO()
        sys.stdout = printed
        cv1 = CalendarView(calendar)
        cv1.display()
        sys.stdout = sys.__stdout__

        return printed.getvalue()

    def handle_calendar_options(self):
        """Handles user inputs in the calendar menu

        VOID
        """

        viewingCalendar = True
        
        while(viewingCalendar):
            
            self.display()
            
            # print initial options
            print(f'Name: {self.calendar.name}')
            print(f'a) Select a Year')
            print(f'b) Exit Program.')
            
            option = input('Select an option (a, b): ')
        
            if option != 'a' and option != 'b':
                print('Invalid option, select again.')
                continue
            
            # take the year input and open up that display
            if option == 'a':
                
                gettingYear = True
                while(gettingYear):
                    year = int(input('Select a year to get started: '))
                
                    if year < self.calendar.years[0].calendarYear or year > self.calendar.years[-1].calendarYear:
                        print('Invalid year, try again.')
                        continue
                    else:
                        gettingYear = False
            
    
                yearToView = self.calendar.years[year - self.calendar.firstYear]
                
                yearViewer = YearView(yearToView)
                yearViewer.handle_year_options(self.calendar)   
            
            # save the progress on this calendar
            if option == 'b':
                viewingCalendar = False

                with open(self.calendar.name + '.txt', 'wb') as f:
                    pickle.dump(self.calendar, f)

        
        

