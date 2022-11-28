
from month import Month
from day import Day
from datetime import date

class Year:

    def __init__(self, calendarYear, leapyear):

        if (type(leapyear) != bool):
            raise TypeError("Invalid argument for parameter leapyear.")

        if (type(calendarYear) != int):
            raise TypeError("Invalid argument for parameter calendarYear.")

        self.calendarYear = calendarYear
        self.leapyear = leapyear
        self.months = []

        MONTHSDICT = { "January" : 31,
        "February" : 28,
        "March" : 31,
        "April" : 30,
        "May" : 31,
        "June" : 30,
        "July" : 31,
        "August" : 31,
        "September" : 30,
        "October" : 31,
        "November" : 30,
        "December" : 31 }

        if leapyear:
            MONTHSDICT["February"] = 29

        # define Months
        for i , (month, numberOfDays) in enumerate(MONTHSDICT):
            self.months.append(Month(month, calendarYear, i, numberOfDays))
