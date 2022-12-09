from Model.calendar import Calendar
from View.year_view import YearView

class CalendarView:

    def __init__(self, calendar: Calendar) -> None:
        self.calendar = calendar
    
    def display(self):
        print(f'Welcome to your Calendar! This is a calendar of your events from {self.calendar.years[0].calendarYear} to {self.calendar.years[-1].calendarYear}!')
    
    def handle_calendar_options(self):
        viewingCalendar = True
        
        while(viewingCalendar):
    
            year = int(input('Select a year to get started!'))
        
            if year < 2000 or year > 2099:
                print("Invalid year, try again.")
                continue
            else:
                yearToView = self.calendar[year - 2000]
                
                yearViewer = YearView(yearToView)
                yearViewer.display()
                yearViewer.handle_year_options(self)        
        
        

