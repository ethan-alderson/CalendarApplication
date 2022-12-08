
from View.day_view import DayView
from Model.day import Day
from Model.event import Event


d1 = Day(2022, 1, 1)
dv1 = DayView(d1)
e1 = Event("Meeting 1", "First meeting", 6, 0, 7, 0)

d1.addEvent(e1)

dv1.display()