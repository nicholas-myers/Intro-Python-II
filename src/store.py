class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments
        
        def __str__(self):
            print(f"Welcome to {self.name}! Which department would you like to visit?")

# should department inherit from store? 
class Department:
    def __init__(self, id, name, products):
        self.id = id
        self.name = name
        self.products = products
        
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        slef.price = price
        
store = Store("Best Buy", 
              [Department(1,"Games", []),
               Department(2,"TVs", []),
               Department(3,"Computers", []),
               Department(4,"Appliances", [])])
# loop forever while browsing departments
# use the input function to prompt user to select a department
while True:
    print(store)