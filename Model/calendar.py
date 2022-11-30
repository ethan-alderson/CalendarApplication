
from year import Year

# represents a calendar
class Calendar:
    
    def __init__(self):
        self.years = {}

    
    def addYear(self, year):
        self.years[year.calendarYear] = year


