# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        
    def print_name(self):
        return f"{self.name}"
    
    def print_room(self):
        return f"You are at the {self.current_room.name}, {self.current_room.description}."
        
    def __str__(self):
        return f"{self.name}, {self.current_room}."