
from .month_view import MonthView
from Model.year import Year

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
        
