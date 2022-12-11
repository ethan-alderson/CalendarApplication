
from Model.month import Month
from Model.year import Year 
from View.day_view import DayView
from View.week_view import WeekView
# from View.year_view import YearView


class MonthView:
    
    def __init__(self, month: Month):
        self.month = month

    def display(self):
        """ Displays the month """
        # print header
        print('-' * 91)
        print('| ' + self.month.name + ' ' * (88 - len(self.month.name)) + '|')
        print('-' * 91)

                
        # print each week
        for week in self.month.weeks:
            for day in week:
                print('| ' + str(day.date.day) + ' ' * (10 - len(str(day.date.day))) + '|', end='')
            print('\r')
            for day in week:
                print('|-----------|', end='')
            print('\r')

            for day in week:

                if len(day.events) == 0:
                    innerString = '         '
                elif len(day.events) == 1:
                    innerString = '1 event  '
                else:
                    innerString = str(len(day.events)) + ' events '

                print('| ' + innerString + ' |', end='')

            print('\r')
            print(len(week) * 13 * '-')
        

    def handle_month_options(self, parentYear: Year):
        """ Handles user inputs for the month

        Args:
            parentYear (Year): year to which this month belongs
        """
        viewingMonth = True
        
        while (viewingMonth):
            
            self.display()
            
            print(f'Month: {self.month.name}')
            print(f'a) View week')
            print(f'b) View day')
            print(f'c) View {parentYear.calendarYear}.')
        
            option = input('Select an option (a, b, c): ')
        
            if option != 'a' and option != 'b' and option != 'c':
                print('Invalid option, select again.')
                continue
            
            if option == 'a':
                
                gettingPosition = True
                while (gettingPosition):
                    position = int(input(f'Which week would you like to view (enter the position in the month, starting at 1): '))
                
                    if position < 0:
                        print('Position cannot be negative.')
                    
                    elif position > len(self.month.weeks):
                        print('Position out of bounds.')
                
                    else:
                        gettingPosition = False
                
                weekViewer = WeekView(self.month.weeks[position - 1])
                weekViewer.handle_week_options(self.month)
                
            if option == 'b':
                
                gettingPosition = True
                while (gettingPosition):
                    position = int(input(f'Which day would you like to view (enter the position in the month, starting at 1): '))
                
                    if position < 0:
                        print('Position cannot be negative.')
                    
                    elif position > len(self.month.days):
                        print('Position out of bounds.')
                
                    else:
                        gettingPosition = False
                
                dayViewer = DayView(self.month.days[position - 1])
                dayViewer.handle_day_options(self.month)
                
            
            if option == 'c':
                viewingMonth = False
