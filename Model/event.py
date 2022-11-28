
from datetime import date, time, datetime

class Event:
    

    # events will be determined either a meeting or a task, then the title will be given, then description, then date, then time of day

    def __init__(self, title, description, datetime):

        if (type(title) != str):
            raise TypeError("Invalid input for title.")

        if (type(description) != str):
            raise TypeError("Invalid input for description.")

        if (type(datetime) != datetime):
            raise TypeError("Invalid input for event's datetime.")


        self.title = title
        self.description = description
        self.datetime = datetime

