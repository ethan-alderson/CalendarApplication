
from .year import Year

# represents a calendar
class Calendar:
    
    def __init__(self, name, firstYear, lastYear):
        self.years = []
        self.name = name
        self.firstYear = firstYear
        self.lastYear = lastYear

        for i in range(firstYear, lastYear + 1):
            self.years.append(Year(i, i % 4))
    