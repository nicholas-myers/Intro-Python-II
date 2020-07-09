# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    # a player can take items from the current room
    def take_item(self, item):
        for i in current_room.items:
            if i == item:
                self.inventory.append(i)
                current_room.items.remove(i)
                
    # a player can drop items into the current room
    def drop_item(self, item):
        for i in self.inventory:
            if i == item:
                self.inventory.remove(i)
                current_room.items.append(i)
    # print the players inventory
    def print_inventory(self):
        if len(self.inventory) == 0:
            print("You currently have no items.")
        elif len(self.inventory) > 0:
            print(f"Inventory: {self.inventory}")
    
    # print players name 
    def print_name(self):
        return f"{self.name}"
    
    def print_room(self):
        return f"You are at the {self.current_room.name},\n {self.current_room.description}.\n"
        
    def __str__(self):
        return f"{self.name}, {self.current_room}."