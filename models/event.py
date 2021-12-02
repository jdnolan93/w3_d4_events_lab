from os import name


class Event():

    def __init__(self, date, name, guest_count, location, description):
        self.date = date
        self.name = name
        self.guest_count = guest_count
        self.location = location
        self.description = description

    def recurring(self, events):
        n = 0
        for event in events:
            if self.name == event.name:
                n +=1

        if n > 1:
            return True
        else:
            return False
        

    