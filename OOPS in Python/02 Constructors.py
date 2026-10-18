# A constructor is a special method in a class used to create and initialize an object of the class .
# Constructor gets called automatically when an object is created of a class. It initialize or assign values to the data members of that class .
# it always return none.

class Person():
    def __init__(self, name, occ):    # __init__ is a constructor that initialize an object of the class 
        self.name = name 
        self.occ = occ

    def intro(self):
        print(f"{self.name} is a {self.occ}.")

a = Person("Shashwat","Student")   # We passed name and occ while creating object . "self" is automatically called, we dont have to do anything .
b = Person("Aman","HR")
a.intro()
b.intro()