# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, loot=None):
        self.name = name
        self.description = description
        self.loot = [] if loot is None else loot
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return('{self.name}, {self.description}, {self.loot}').format(self=self)

    # add item to room inventory/loot
    def add_item(self, item):
        self.loot.append(item)

    # remove item from room inventory/loot
    def remove_item(self, item):
        self.loot.remove(item)
