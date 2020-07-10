# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        
    def print_items(self):
        item_names = []
        for i in self.items:
            item_names.append(i.__str__())
        print("You see the following items: ")
        print(f"{item_names}\n")
    
    def __str__(self):
        return f"{self.name}, {self.description}."