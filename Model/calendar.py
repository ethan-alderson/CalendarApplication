
from .year import Year

# represents a calendar
class Calendar:
    """Represents a Calendar
    """
    def __init__(self, name, firstYear, lastYear):
        self.years = []
        self.name = name

        for i in range(firstYear, lastYear + 1):
            self.years.append(Year(i))
    