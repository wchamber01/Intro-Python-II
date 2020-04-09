# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, room_inventory=None):
        self.name = name
        self.description = description
        self.room_inventory = [] if room_inventory is None else room_inventory
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        
    def __str__(self):
        return('{self.name}, {self.description}, {self.room_inventory}').format(self=self)