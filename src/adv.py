from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# for r, value in room.items():
    # print(value.__str__())
# Link rooms together

room['outside'].n_to = room['foyer']
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
print(f"Welcome Adventurer {player.print_name()}! {player.print_room()}")
print(f"You see {player.current_room.items}")
print(f"Possible actions: 'n' for North, 's' for south, 'e' for East, 'w' for West")
print(f"To exit: 'q', 'quit', or 'exit'")   
def nomove():
    print("You can't go that way")
    print(f"{player.print_room()}")
    
while True:
    action = input("What action do you take? ")
        # check the current room and perform
    if action == "n":
        # print(f"{player.current_room.n_to}")
        try:
            player.current_room = player.current_room.n_to
            print(f"{player.print_room()}")
        except:
            nomove()
    elif action == "s":
        try:
            player.current_room = player.current_room.s_to
            print(f"{player.print_room()}")
        except:
            nomove()
    elif action == "w":
        try:
            player.current_room = player.current_room.w_to
            print(f"{player.print_room()}")
        except:
            nomove()
    elif action == "e":
        try:
            player.current_room = player.current_room.e_to
            print(f"{player.print_room()}")
        except:
            nomove()
    elif action == "q" or action == "quit" or action == "exit":
        break
    else:
        print("I don't understand that command ><!")
        
        