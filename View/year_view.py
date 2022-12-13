
import sys
import io

from .month_view import MonthView
from Model.year import Year
from Model.calendar import Calendar


class YearView:
    """Represents the UI for the given year
    """
    def __init__(self, year: Year):
        self.year = year
        
    def display(self):
        # print header
        print('-' * 91)
        print('| ' + str(self.year.calendarYear) + ' ' * (88 - len(str(self.year.calendarYear))) + '|')
        print('-' * 91)
        
        for month in self.year.months:
            mv = MonthView(month)
            mv.display()

    @staticmethod
    def testDisplay(year: Year):
        """test method, all it does is run display but reroute the print statement into a StringIO object. 
        It does this so that we can check the display output in our tests even though it only prints to the console.

        Args:
            year (Year): The year to display

        Returns:
            String: The entire display in a single string
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        yv1 = YearView(year)
        yv1.display()
        sys.stdout = sys.__stdout__

        return capturedOutput.getvalue()
            
        
    def handle_year_options(self, parentCalendar: Calendar):
        """Handles the user inputs for the current yearview

        Args:
            parentCalendar (Calendar): the calendar that this year came from
        """
        viewingYear = True
        
        while (viewingYear):
            
            self.display()
            
            print(f'Year: {self.year.calendarYear}')
            print(f'a) View a month')
            print(f'b) Go Back.')
        
            option = input('Select an option (a, b): ')
        
            if option != 'a' and option != 'b':
                print('Invalid option, select again.')
                continue
            
            # transition to the monthview that they want
            if option == 'a':
                
                gettingPosition = True
                
                while (gettingPosition):
                    position = int(input(f'Which month would you like to view (enter the position in the year, starting at 1): '))
                
                    if position < 0:
                        print('Position cannot be negative.')
                    
                    elif position > 12:
                        print('Position out of bounds.')
                    else:
                        gettingPosition = False
                
                
                monthViewer = MonthView(self.year.months[position - 1])
                monthViewer.handle_month_options(self.year)
            
            # exit the current view, going back to the previous calendar view
            if option == 'b':
                viewingYear = False