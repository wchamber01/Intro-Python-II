# Write a class to hold player information, e.g. name, what room they are in
# currently, etc.

class Player:
    def __init__(self, name, health, room, inventory=None, armor_on=None, weapon_on=None):
        self.name = name
        self.health = health
        self.protection = protection
        self.room = room
        self.inventory = [] if inventory is None else inventory
        self.armor_on = None if armor_on is None else armor_on
        self.weapon_on = None if weapon_on is None else weapon_on
    
    def __str__(self):
        return('{self.name}, {self.health}, {self.protection}, {self.room}, {self.inventory}, {self.armor_on}, {self.weapon_on}').format(self=self)

    # add item to player inventory
    def add_item(self, item):
        self.inventory.append(item)
    
    # remove item from player inventory
    def drop_item(self, item):
        self.inventory.remove(item)
        ''' **** pseudo code ***
        if item to be dropped matches Healing item with protection level
        then self.protection = self.protection-item.protection 
        
        for i in self.inventory:
            if 
        
        
        '''
        
    
    # apply armor inventory item to player i.e. put on/use armor item
    def use_armor(self, item):
        self.armor_on = item
        self.protection = self.protection+item.protection
        print('Your protection level is : ',self.protection,'.')
    
    # stash armor item from use - *Required before drop_item
    def stash_armor(self, item):
        self.armor_on = None
        self.protection = self.protection-item.protection
        print('Your protection level is : ',self.protection,'.')
    
    # apply healing inventory item to player i.e. use/eat healing item
    def use_healing(self, item):
        self.health = self.health+item.health
        self.protection = self.protection+item.protection
        print('Your health is now : ',self.health,'.')
        print('Your protection level is : ',self.protection,'.')
    
    # equip/ready weapon inventory item onto player i.e. hold/ready weapon item
    def ready_weapon(self, item):
        self.weapon_on = item
