from room import Room
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item("Wood Sword", "The blade and hilt are made of wood, it looks like a fine carpenter wittled this, it's edges are dulled and look as if it could not cut through anything.")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [Item("Wood Sword", "The blade and hilt are made of wood, it looks like a fine carpenter wittled this, it's edges are dulled and look as if it could not cut through anything.")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [Item("Wood Sword", "The blade and hilt are made of wood, it looks like a fine carpenter wittled this, it's edges are dulled and look as if it could not cut through anything.")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [Item("Wood Sword", "The blade and hilt are made of wood, it looks like a fine carpenter wittled this, it's edges are dulled and look as if it could not cut through anything.")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [Item("Wood Sword", "The blade and hilt are made of wood, it looks like a fine carpenter wittled this, it's edges are dulled and look as if it could not cut through anything.")]),
}
# for r, value in room.items():
    # print(value.__str__())
# Link rooms together

room['outside'].n_to = room['foyer']
print(f"{room['outside'].items}")
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# ######### MAIN ############

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# ######### MOVEMENT ############
# print a intro message
# intro welcomes player and tells them the current room
# the player starts outside
# you are [location] available commands n, s, e, w
# add error messages when trying to move where there is no room


# ######### ITEMS ############
# add a list of items to each room and player that are seperate from each other
# add items to each room
# give player ability to drop or pickup items
# to pickup
# loop over the list of items in the room
# remove the item from the room
# add item to the player

from player import Player


player_name = input("Enter your name to play: ")
# print(room["outside"])
player = Player(player_name, room["outside"])
print(f"\nWelcome Adventurer {player.print_name()}! \n{player.print_room()}")
print(f"Possible actions:\n 'n' for North,\n 's' for south,\n 'e' for East,\n 'w' for West\n")
print(f"To exit: 'q', 'quit', or 'exit'\n")   
move = ["n", "s", "e", "w"]
exit = ["q", "quit", "exit"]
def nomove():
    print("You can't go that way!\n")
    print(f"{player.print_room()}")
    
while True:
    action = input("What action do you take? ")
        # check the current room and perform
        # dynamically 
    if [close for close in exit if action == close]:
        print(f"Come play again Adventurer {player_name}!")
        break
    for direction in move:
        if action == direction:
            moved = direction + "_to"
            try:
                player.current_room = getattr(player.current_room, moved)
                print(f"{player.print_room()}")
            except:
                nomove()
    else:
        print("I don't understand that command ><!")
        print(f"Possible actions:\n 'n' for North,\n 's' for south,\n 'e' for East,\n 'w' for West\n")
 
        