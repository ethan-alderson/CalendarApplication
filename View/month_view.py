
from Model.month import Month
from Model.year import Year 

class MonthView:
    
    def __init__(self, month: Month):
        self.month = month
        self.weeks = []
        
        # break the month into 7 day blocks
        for i in range(1, 6):
            if len(self.month.days) >= i * 7:
                self.weeks.append(self.month.days[(i-1)*7:(i*7)])
            else:
                self.weeks.append(self.month.days[(i-1)*7:])
                

    def display(self):
        
        # print header
        print("-" * 91)
        print("| " + self.month.name + " " * (88 - len(self.month.name)) + "|")
        print("-" * 91)
                
        # print each week
        for week in self.weeks:
            for day in week:
                print('| ' + str(day.date.day) + ' ' * (10 - len(str(day.date.day))) + '|', end="")
            print('\r')
            for day in week:
                print("|-----------|", end="")
            print('\r')
            for day in week:
                print("| Events: " + str(len(day.events)) + " |", end="")
            print('\r')
            print(len(week) * 13 * "-")
        

    def handle_month_options(self, parentYear: Year):
        print(f'Month: {self.month.name}')
        print(f'a) View week')
        print(f'b) View day')
        print(f'c) View {parentYear}.')