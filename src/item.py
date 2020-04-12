# Write a class to hold item information, e.g. torch, sword, shield, etc.
# This should have name and description attributes.
# The name should be one word for ease in parsing later.
#This will be the _base class_ for specialized item types to be declared later.

#General items category
class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.in_use = False
    
    def __str__(self):
        return('{self.name}, {self.desc}').format(self=self)

#Food and medicine items - *Increases health and protection depending on item
class Healing(Item):
    def __init__(self, name, desc, health, protection):
        super().__init__(name, desc)
        self.health = health
        self.protection = protection
    
    def __str__(self):
        return('{self.name}, {self.desc}, {self.health}, {self.protection}').format(self=self)

#All weapon items - *Inflicts damage
class Weapon(Item):
    def __init__(self, name, desc, damage):
        super().__init__(name, desc)
        self.damage = damage
    
    def __str__(self):
        return('{self.name}, {self.desc}, {self.damage}').format(self=self)

#All armor items - *Adds protection factor
class Armor(Item):
    def __init__(self, name, desc, protection):
        super().__init__(name, desc)
        self.protection = protection        
    
    def __str__(self):
        return('{self.name}, {self.desc}, {self.protection}').format(self=self)