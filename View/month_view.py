
from Model.month import Month
from Model.year import Year 
from View.day_view import DayView
from View.week_view import WeekView
# from View.year_view import YearView


class MonthView:
    
    def __init__(self, month: Month):
        self.month = month

    def display(self):
        
        # print header
        print("-" * 91)
        print("| " + self.month.name + " " * (88 - len(self.month.name)) + "|")
        print("-" * 91)
                
        # print each week
        for week in self.month.weeks:
            for day in week:
                print('| ' + str(day.date.day) + ' ' * (10 - len(str(day.date.day))) + '|', end="")
            print('\r')
            for day in week:
                print("|-----------|", end="")
            print('\r')
            for day in week:
                print("| Events: " + str(len(day.events)) + " |", end="")
            print('\r')
            print(len(week) * 13 * "-")
        

    def handle_month_options(self, parentYear: Year):

        viewingMonth = True
        
        while (viewingMonth):
                
            print(f'Month: {self.month.name}')
            print(f'a) View week')
            print(f'b) View day')
            print(f'c) View {parentYear}.')
        
            option = input('Select an option (a, b, c): ')
        
            if option != 'a' and option != 'b' and option != 'c':
                print('Invalid option, select again.')
                continue
            
            if option == 'a':
                
                gettingPosition = True
                while (gettingPosition):
                    position = int(input(f'Which week would you like to view (enter the position in the month, starting at 1): '))
                
                if position < 0:
                    print("Position cannot be negative.")
                    
                if position > len(self.month.weeks):
                    print("Position out of bounds.")
                
                weekViewer = WeekView(self.month.weeks[position - 1])
                weekViewer.display()
                weekViewer.handle_week_options()
                
            if option == 'b':
                
                gettingPosition = True
                while (gettingPosition):
                    position = int(input(f'Which day would you like to view (enter the position in the month, starting at 1): '))
                
                if position < 0:
                    print("Position cannot be negative.")
                    
                if position > len(self.month.days):
                    print("Position out of bounds.")
                
                dayViewer = DayView(self.days[position - 1])
                dayViewer.display()
                dayViewer.handle_day_options()
                
            
            if option == 'c':
                viewingMonth = False
                # yearViewer = YearView(parentYear)
                # yearViewer.display()
                # yearViewer.handle_year_options()