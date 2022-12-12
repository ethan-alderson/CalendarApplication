
import unittest
from Model.calendar import Calendar
from View.calendar_view import CalendarView

class testCalendarDisplay(unittest.TestCase):

# print(f'Welcome to your Calendar! This is a calendar of your events from {self.calendar.years[0].calendarYear} to {self.calendar.years[-1].calendarYear}!')

    def test_standard(self):

        calendar1 = Calendar('Test_Calendar', 2021, 2025)
        
        calendar1.display()

        unittest.mock_print.assert_called_with(f'Welcome to your Calendar! This is a calendar of your events from 2021 to 2025!')
