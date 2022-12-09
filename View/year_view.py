
from .month_view import MonthView
from Model.year import Year
from Model.calendar import Calendar

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
        print(f'Date: {self.day.date}')
        print(f'a) Add Event')
        print(f'b) Remove Event')
        print(f'c) View {parentCalendar.name}.')