# A constructor is a special method in a class used to create and initialize an object of the class .
# Constructor gets called automatically when an object is created of a class. It initialize or assign values to the data members of that class .
# it always return none.

class Person:
    def __init__(self, name, occ):    # __init__ is a parameter constructor that initialize an object of the class 
        self.name = name 
        self.occ = occ

    def intro(self):
        print(f"{self.name} is a {self.occ}.")

a = Person("Shashwat","Student")   # We passed name and occ while creating object . "self" is automatically called, we dont have to do anything .
b = Person("Aman","HR")
a.intro()
b.intro()

# Default constructor 
# When the const doesnt accept any arguments from the object and only has one argument "self".

class Player:
    def __init__(self):
        print("This is info about player")
ram = Player()
raghu = Player()
ram.health = 100
raghu.health = 90
print(ram.health, raghu.health)

# we use default when we have to add attributes later . 
# for ex: shopping cart , initially it is empty but it gets filled and total items increase as we add items to it.