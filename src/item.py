# Write a class to hold item information, e.g. torch, sword, shield, etc.
# This should have name and description attributes.
# The name should be one word for ease in parsing later.
#This will be the _base class_ for specialized item types to be declared later.

class Item:
    def __init__(self, name, health, desc):
        self.name = name
        self.health = health
        self.desc = desc

# class Food(Item):
#     def __init__(self, health):
#         super().__init__(name)
#         self.health = health
        
# class Weapon(Item):
#     def __init__(self, damage):
#         super().__init__(name)
#         self.damage = damage