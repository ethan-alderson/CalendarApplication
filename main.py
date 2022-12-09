
# from View import day_view
# from View import month_view
# from View import week_view
# from Model.day import Day
# from Model.event import Event
# from Model.month import Month
# from Model.year import Year
# from View import year_view
from View import calendar_view
from Model.calendar import Calendar


# d1 = Day(2022, 1, 1)
# dv1 = day_view.DayView(d1)
# tooLong = "*" * 26

# # e1 = Event(tooLong, "First meeting", 6, 0, 7, 0)
# e2 = Event("Meeting 2", "First meeting", 14, 15, 16, 30)
# e3 = Event("Conflicting meeting", "First meeting", 15, 0, 17, 0)

# # d1.addEvent(e1)
# d1.addEvent(e2)
# d1.addEvent(e3)

# # dv1.display()

# m1 = Month("January", 2022, 1, 28)

# mv1 = month_view.MonthView(m1)

# # mv1.display()

# wv1 = week_view.WeekView(m1.days[:7])
# # wv1.display()

# y1 = Year(2022, True)
# yv1 = year_view.YearView(y1)
# # yv1.display()

calendar1 = Calendar("Test Calendar")
cv1 = calendar_view.CalendarView(calendar1)

cv1.display()
cv1.handle_calendar_options()