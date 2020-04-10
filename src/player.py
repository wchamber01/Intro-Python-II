# Write a class to hold player information, e.g. name, what room they are in
# currently, etc.

class Player:
    def __init__(self, name, health, room, inventory=None):
        self.name = name
        self.health = health
        self.room = room
        self.inventory = [] if inventory is None else inventory
    
    def __str__(self):
        return('{self.name}, {self.health}, {self.room}').format(self=self)
      
    def add_item(self, item):
        self.inventory.append(item)
    
    def drop_item(self, item):
        self.inventory.remove(item)