
from year import Year

# represents a calendar
class Calendar:
    
    def __init__(self, year):
        
        if (type(year) != year):
            raise TypeError("Calendar argument must be a year.")
