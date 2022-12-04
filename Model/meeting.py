
from event import Event

class Meeting(Event):

    def __init__(self, title, description, datetime, recipient):
        super().__init__(title, description, datetime)

        # could introduce a recipient class?
        self.recipient = recipient
