from room import Room
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item("Wood Sword", "The blade and hilt are made of wood, it looks like a fine carpenter wittled this, it's edges are dulled and look as if it could not cut through anything."), Item("Wood Shield", "The workmanship is similar to the wood sword, this won't protect you against any flames.")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [Item("Shiny Helmet", "A metal helm, with a shiny silver sheen."), Item("Bronze Breastplate", "A golden brown chest piece.")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [Item("Red Cloak", "You see a skeleton, with a battered cloak.")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [Item("Torch", "Hooked on the wall is a lont metal stick, with a metal cage carrying a flame")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [Item("Health Potion", "There is no gold in here but you do find a bottle with a strange purple liquid.")]),
}
# for r, value in room.items():
    # print(value.__str__())
# Link rooms together

room['outside'].n_to = room['foyer']
# print(f"{room['outside'].items}")
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
# a player should see the items in each room
# a player should be able to see the items in their inventory
# should the item passed through be the entire item or just the name?
# how does the program know you are trying to pick up an item
# take the input check if it 

from player import Player

# capture the player name
player_name = input("Enter your name to play: ")
# create the player and place them on the map
player = Player(player_name, room["outside"])
# welcome the player into the game and give them info
print(f"\nWelcome Adventurer {player.print_name()}! \n{player.print_room()}")
player.print_inventory()
player.current_room.print_items()
def possible_actions():
    print(f"Move:\n 'n' for North, 's' for south, 'e' for East, 'w' for West")
    print(f"Actions:\n 'take [item]' to pick up an item, 'drop [item]' to drop an item in your inventory\n")
    print(f"To exit: 'q', 'quit', or 'exit'\n")   
possible_actions()
# define the actions
directions = ["n", "s", "e", "w"]
exit = ["q", "quit", "exit"]
def nomove():
    print("\nYou can't go that way!\n")
    print(f"{player.print_room()}")
    print("You see the following items: ")
    player.current_room.print_items()

########### GAME FLOW ###############
while True:
    action = input("What action do you take? ").split(" ")
    if len(action) == 1:
        action = action[0]
        if [close for close in exit if action == close]:
            print(f"Come play again Adventurer {player_name}!")
            break
        elif [move for move in directions if action == move]:
                for move in directions:
                    if action == move:
                        moved = move + "_to"
                        try:
                            player.current_room = getattr(player.current_room, moved)
                            print(f"\n{player.print_room()}")
                            print("You see: ")
                            player.current_room.print_items()
                        except:
                            nomove()
        else:
            print("I don't understand that ><!\n")
            possible_actions()
    elif len(action) >= 2:
        find_list = [word for word in action if word != action[0]]
        find_word = " ".join(find_list)
        # print(find_word)
        if action[0] == "take":
            player.take_item(find_word)
            print(f"{player.print_room()}")
            player.print_inventory()
            player.current_room.print_items()
        elif action[0] == "drop":
            player.drop_item(find_word)
            print(f"{player.print_room()}")
            player.print_inventory()
            player.current_room.print_items()