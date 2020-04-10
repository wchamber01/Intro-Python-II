# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, inventory=None):
        self.name = name
        self.description = description
        self.inventory = [] if inventory is None else inventory
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        
    def __str__(self):
        return('{self.name}, {self.description}, {self.inventory}').format(self=self)
      
    def add_item(self, item):
        self.inventory.append(item)
    
    def drop_item(self, item):
        self.inventory.remove(item)