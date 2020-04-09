# Write a class to hold player information, e.g. name, what room they are in
# currently, etc.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.location_info = None
        self.health = 100
        self.inventory = []
    
    def __str__(self):
        return('{self.name}, {self.location}, {self.location_info}').format(self=self)