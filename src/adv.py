from room import Room
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

# Declare all the rooms

room = {
    'outside':  Room("Outside", "You are now outside the cave entrance. North of you, the cave mouth beckons.\n"),

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

#
# Main
#

# Welcome message
print('You have started Jumanji Quarantine Version!')
cmd = input("If you don't fear for your life, press 'Enter' to continue, otherwise press 'Q' + 'Enter' to abort.\n").lower()
print(cmd)
if cmd == 'q':
    exit(0)
else:
    pass

# Make a new player object that is currently in the 'outside' room.
player_name = input("Enter player's name: ")
player = Player(player_name, 100, room['outside'])
#print('initialize',player)
print('\nWelcome, ' + player.name + '! Your health is '+str(player.health)+'%.\nYou have landed outside.\nNorth of you, the cave mouth beckons.\nChoose a direction to start exploring.\n')


# Write a loop that:
while True:

    def no_enter():
        print("Can't go that way!")

    def describe():
        print('Current room: '+ player.room.name)
        print('Description:'+ player.room.description)

    key = input("Enter [N] North,  [S] South,  [E] East, or [W] West to move player.\n").lower()
    if key == 'q':
        break
    # describe()
    
    # player chooses North
    elif key == 'n':
        if player.room.n_to != None:
            player.room == player.room.n_to
            print('player room inside loop',player.room.name)
            describe()
        else:
            no_enter()
    # player chooses North
    elif key == 's':
        if player.room.s_to != None:
            player.room == player.room.s_to
            # describe()
        else:
            no_enter()
    # player chooses East
    elif key == 'e':
        if player.room.e_to != None:
            player.room == player.room.e_to
            # describe()
        else:
            no_enter()
    # player chooses West
    elif key == 'w':
        if player.room.w_to != None:
            player.room == player.room.w_to
            # describe()
        else:
            no_enter()
    else:
        print('Invalid entry. Please try again.')
        # exit(0)

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