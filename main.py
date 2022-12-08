
from view import day_view
from model.day import Day
from model.event import Event

d1 = Day(2022, 1, 1)
dv1 = day_view.DayView(d1)
tooLong = "*" * 26

# e1 = Event(tooLong, "First meeting", 6, 0, 7, 0)
e2 = Event("Meeting 2", "First meeting", 14, 15, 16, 30)
e3 = Event("Conflicting meeting", "First meeting", 15, 0, 17, 0)

# d1.addEvent(e1)
d1.addEvent(e2)
d1.addEvent(e3)

dv1.display()