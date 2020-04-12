from room import Room
from item import *
from player import Player
import random
import textwrap

# Create save file
# def load_results():
#     text_file = open("saved.txt", "r")
#     saved = text_file.read().split(",")
#     text_file.close()
#     return saved

# def save_results(w):
#     text_file = open("saved.txt", "w")
#     text_file.write(str(w))
#     text_file.close()

# Declare all the items

item = {                #Name           #Description
    'thieves': Healing("Thieves", """An ancient blend of spices rumored to cure the dreaded Corona Virus.""",25,2),
    
    'mask': Armor("Mask", """An N95 facemask sitting on a lone table.""",1),
    
    'torch': Item("Torch", """A burning torch hanging on the wall""")
}

# Declare all the rooms

room = {                #Name           #Description
    'outside':  Room("Outside", """You are now outside the cave entrance. North of you, the cave mouth beckons.\n"""),

    'foyer':    Room("Foyer", """You have entered the Foyer. Dim light filters in from the south. Dusty passages run north and east.\n"""),

    'overlook': Room("The Grand Overlook", """You are at The Grand Overlook. A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.\n"""),

    'narrow':   Room("Narrow Passage", """Entering from the west, the long narrow passage appears to bend towards the north. The smell of gold permeates the air.\n"""),

    'treasure': Room("The Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.\n"""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms

room['foyer'].add_item(item['thieves'])
room['overlook'].add_item(item['mask'])
room['narrow'].add_item(item['torch'])

#
# Main
#

# Welcome message

print('\n\nYou have started Jumanji Quarantine Version!\n')
cmd = input("If you don't fear for your life, press 'Enter' to continue, otherwise press 'Q' + 'Enter' to abort.\n").lower()
print(cmd)
if cmd == 'q':
    print('Goodbye!')
    exit(0)
else:
    pass


# Make a new player object that is currently in the 'outside' room.

player_name = input("Enter player's name: ")
player = Player(player_name, 100, room['outside'])

print('\nWelcome, ' + player.name + '! Your health is '+str(player.health)+'%.\nYour protection level is '+str(player.protection)+'/10.\nYou have landed outside.\nNorth of you, the cave mouth beckons.\nChoose a direction to start exploring.\n')


# Write a loop that:
while True:

    def no_enter():
        print("Can't go that way!")

    def describe():
        print('Current room: '+ player.room.name)
        print('Description:'+ player.room.description)
        if len(player.room.loot) > 0:
            for item in player.room.loot:
                print("You have found ",item,". Type 'get [item name]' to add item to your collection.")
        else:
            pass
    key = input("Enter [N] North,  [S] South,  [E] East, or [W] West to move player.\n").lower()
    if key == 'q':
        print('Goodbye!')
        break
    
    elif key == 'status' or key == 'stat':
        print('Stats: ',player)
    
    elif key == 'h' or key == 'health':
        print(player.health)
    
    elif key == 'i' or key == 'info':
        for i in player.inventory:
            if len(player.inventory) == 0:
                print('There are no items in your inventory.')
            else:
                print('Current Inventory: ',i.name)
    
    elif len(key.split()) == 2:
        action_handler = key.split()
        
        if action_handler[0] == 'take' or action_handler[0] == 'get':
            target_item = action_handler[1]
            found=False
            for i in player.room.loot:
                if i.name.lower() == target_item.lower():
                    found = True
                    player.add_item(i)
                    player.room.remove_item(i)
                    print('You have added ',i.name,'to your inventory. What is your next move?')
            if found == False:
                print("Error: Invalid entry or item does not exist.")   
            else:
                found = False
        
        elif action_handler[0] == 'drop' or action_handler[0] == 'remove':
            target_item = action_handler[1]
            found=False
            if player.armor_on == None or player.armor_on.name.lower() != target_item.lower():
                for i in player.inventory:
                    if i.name.lower() == target_item.lower():
                        found = True
                        player.drop_item(i)
                        player.room.add_item(i)
                        print('You have dropped ',i.name,'. Choose your next move.')
                if found == False:
                    print("Error: Invalid entry or item does not exist.")  
                else:
                    found = False
            else:
                print('Stash armor before dropping.')
        
        elif action_handler[0] == 'equip' or action_handler[0 == 'apply']:
            target_item = action_handler[1]
            found=False
            for armor in player.inventory:
                if armor.name.lower() == target_item.lower():
                    found = True
                    player.use_armor(armor)
                    print('You have equipped ',armor.name,'. Choose your next move.')
            if found == False:
                print("Error: Invalid entry or item does not exist.")  
            else:
                found = False
        
        elif action_handler[0] == 'stash' or action_handler[0] == 'lose':
            target_item = action_handler[1]
            found=False
            # if player.weapon_on == None or player.weapon_on.name.lower() !=  target_item.lower():
            for armor in player.inventory:
                if armor.name.lower() == target_item.lower():
                    found = True
                    player.remove_armor(armor)
                    print('You have stashed ',armor.name,'. Choose your next move.')
            if found == False:
                print("Error: Invalid entry or item does not exist.")  
            else:
                found = False
            # else:
            #     print('Remove armor before dropping')
    
    # player chooses North
    elif key == 'n' or key == 8 or key == '\x1b[A':
        if player.room.n_to != None:
            player.room = player.room.n_to
            describe()
            
        else:
            no_enter()
    
    # player chooses South
    elif key == 's' or key == 2 or key == '\x1b[B':
        if player.room.s_to != None:
            player.room = player.room.s_to
            describe()
        else:
            no_enter()
    
    # player chooses East
    elif key == 'e' or key == 6 or key == '\x1b[C':
        if player.room.e_to != None:
            player.room = player.room.e_to
            describe()
        else:
            no_enter()
    
    # player chooses West
    elif key == 'w' or key == 4 or key == '\x1b[D':
        if player.room.w_to != None:
            player.room = player.room.w_to
            describe()
        else:
            no_enter()
    
    else:
        print('Invalid entry. Please try again.')

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
'''
* Add a REPL parser to `adv.py` that accepts directional commands to move the player
  * After each move, the REPL should print the name and description of the player's current room
  * Valid commands are `n`, `s`, `e` and `w` which move the player North, South, East or West
  * The parser should print an error if the player tries to move where there is no room.
  '''