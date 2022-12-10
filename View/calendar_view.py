from Model.calendar import Calendar
from View.year_view import YearView
import pickle


class CalendarView:

    def __init__(self, calendar: Calendar) -> None:
        self.calendar = calendar
    
    def display(self):
        print(f'Welcome to your Calendar! This is a calendar of your events from {self.calendar.years[0].calendarYear} to {self.calendar.years[-1].calendarYear}!')
    
    def handle_calendar_options(self):
        viewingCalendar = True
        
        while(viewingCalendar):
            
            self.display()
            
            print(f'Name: {self.calendar.name}')
            print(f'a) Select a Year')
            print(f'b) Exit Program.')
            
            option = input('Select an option (a, b): ')
        
            if option != 'a' and option != 'b':
                print('Invalid option, select again.')
                continue
            
            if option == 'a':
                
                gettingYear = True
                while(gettingYear):
                    year = int(input('Select a year to get started: '))
                
                    if year < 2000 or year > 2099:
                        print("Invalid year, try again.")
                        continue
                    else:
                        gettingYear = False
            
        
                yearToView = self.calendar.years[year - self.calendar.firstYear]
                
                yearViewer = YearView(yearToView)
                yearViewer.handle_year_options(self.calendar)   
            
            if option == 'b':
                viewingCalendar = False

                with open(self.calendar.name + ".txt", 'wb') as f:
                    pickle.dump(self.calendar, f)

        
        

