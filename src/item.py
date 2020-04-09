# Write a class to hold item information, e.g. torch, sword, shield, etc.
# This should have name and description attributes.
# The name should be one word for ease in parsing later.
#This will be the _base class_ for specialized item types to be declared later.

class Item:
    def __init__(self, item_name, item_desc):
        self.item_name = item_name
        self.item_desc = item_desc

class Food(Item):
    def __init__(self, health, item_name):
        super().__init__(item_name)
        self.health = health
        
class Weapon(Item):
    def __init__(self, damage, item_name):
        super().__init__(item_name)
        self.damage = damage