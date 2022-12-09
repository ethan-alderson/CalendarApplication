
from .month_view import MonthView
from Model.year import Year
from Model.calendar import Calendar
# from View.calendar_view import CalendarView

class YearView:
    
    def __init__(self, year: Year):
        self.year = year
        
    def display(self):
        # print header
        print("-" * 91)
        print("| " + str(self.year.calendarYear) + " " * (88 - len(str(self.year.calendarYear))) + "|")
        print("-" * 91)
        
        for month in self.year.months:
            mv = MonthView(month)
            mv.display()
        

    def handle_year_options(self, parentCalendar: Calendar):
        
        viewingYear = True
        
        while (viewingYear):
                
            print(f'Year: {self.year.calendarYear}')
            print(f'a) View a month')
            print(f'b) View {parentCalendar.name}.')
        
            option = input('Select an option (a, b, c): ')
        
            if option != 'a' and option != 'b' and option != 'c':
                print('Invalid option, select again.')
                continue
            
            if option == 'a':
                
                gettingPosition = True
                while (gettingPosition):
                    position = int(input(f'Which month would you like to view (enter the position in the year, starting at 1): '))
                
                if position < 0:
                    print("Position cannot be negative.")
                    
                if position > 12:
                    print("Position out of bounds.")
                
                monthViewer = MonthView(self.year.months[position - 1])
                monthViewer.display()
                monthViewer.handle_month_options()
                
            if option == 'b':
                viewingYear = False
                # calendarViewer = CalendarView(parentCalendar)
                # calendarViewer.display()
                # calendarViewer.handle_calendar_options()