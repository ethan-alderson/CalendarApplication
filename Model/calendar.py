
from year import Year

# represents a calendar
class Calendar:
    
    def __init__(self, name):
        self.years = []

        for i in range(99):
            self.years.append(Year(2000 + i, (2000 + i) % 4))
    