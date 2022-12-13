
import io
import sys

import unittest

from Model.calendar import Calendar
from View.calendar_view import CalendarView

from View.year_view import YearView
from Model.year import Year

from View.month_view import MonthView
from Model.month import Month

from View.week_view import WeekView

from View.day_view import DayView
from Model.day import Day


class testCalendarDisplay(unittest.TestCase):
    """tests for Calendar.display()
    """
    def test_standard(self):

        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1
        calendar1 = Calendar('Test_Calendar', 2021, 2025)
        calendar1View = CalendarView(calendar1)
        calendar1View.display()

        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        calendar2 = Calendar('Second_Test_Calendar', 2022, 2026)
        calendar2View = CalendarView(calendar2)
        calendar2View.display()

        sys.stdout = sys.__stdout__

        self.assertEqual(capturedOutput1.getvalue(), CalendarView.testDisplay(calendar1))
        self.assertEqual(capturedOutput2.getvalue(), CalendarView.testDisplay(calendar2))

        # self.assertEqual(calendar1View.display(), 'Welcome to your Calendar! This is a calendar of your events from 2021 to 2025!')
        # self.assertEqual(calendar2View.display(), 'Welcome to your Calendar! This is a calendar of your events from 2022 to 2026!')

class testYearDisplay(unittest.TestCase):
    """tests for Year.display()
    """
    def test_standard_year_display(self):
        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1
        year1 = Year(2021)
        yv1 = YearView(year1)
        yv1.display()

        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        year2 = Year(2023)
        yv2 = YearView(year2)
        yv2.display()

        sys.stdout = sys.__stdout__

        self.assertEqual(capturedOutput1.getvalue(), YearView.testDisplay(year1))
        self.assertEqual(capturedOutput2.getvalue(), YearView.testDisplay(year2))

class testMonthDisplay(unittest.TestCase):
    """tests for Month.display()
    """
    def test_standard_month_display(self):
        
        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1
        month1 = Month("January", 2022, 1, 31)
        mv1 = MonthView(month1)
        mv1.display()

        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        month2 = Month("February", 2023, 2, 28)
        mv2 = MonthView(month2)
        mv2.display()

        sys.stdout = sys.__stdout__

        self.assertEqual(capturedOutput1.getvalue(), MonthView.testDisplay(month1))
        self.assertEqual(capturedOutput2.getvalue(), MonthView.testDisplay(month2))

class testWeekDisplay(unittest.TestCase):
    """tests for week display()
    """
    def test_standard_month_display(self):
        
        month1 = Month("January", 2022, 1, 31)

        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1
        week1 = month1.weeks[0]
        wv1 = WeekView(week1)
        wv1.display()

        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        week2 = month1.weeks[1]
        wv2 = WeekView(week2)
        wv2.display()

        sys.stdout = sys.__stdout__

        self.assertEqual(capturedOutput1.getvalue(), WeekView.testDisplay(week1))
        self.assertEqual(capturedOutput2.getvalue(), WeekView.testDisplay(week2))

class testDayDisplay(unittest.TestCase):
    """tests for Day.display()
    """
    def test_standard_month_display(self):

        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1
        day1 = Day(2022, 2, 2)
        dv1 = DayView(day1)
        dv1.display()

        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        day2 = Day(2023, 3, 2)
        dv2 = DayView(day2)
        dv2.display()

        sys.stdout = sys.__stdout__

        self.assertEqual(capturedOutput1.getvalue(), DayView.testDisplay(day1))
        self.assertEqual(capturedOutput2.getvalue(), DayView.testDisplay(day2))