
from .day import Day
from datetime import date

class Month:

    # Constructor for a month, in a year, containing a certain number of empty days
    def __init__(self, name, year, monthNumber, monthLength):

        self.name = name
        self.days = []
        self.monthNumber = monthNumber
        self.monthLength = monthLength

        if (monthNumber > 12):
            raise ValueError("Cannot have a year with monthNumber greater than 12.")

        if (monthLength != 28 and monthLength != 29 and monthLength != 30 and monthLength != 31):
            raise ValueError("Invalid input for monthLength.")
        
        # fill the month with empty days of the correct date
        for i in range(monthLength):
            self.days.append(Day(year, monthNumber, i + 1))