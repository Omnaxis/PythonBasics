# class contains attributes and methods , it is a blueprint of the object.
# object is a instance of class . It is a entity made from class contaning the functions and data of the class .

class Person:              # We  created a class - "Person" using class keyword
    name = "Shashwat"
    occ = "Student"
    net = 1000
    def info(self):       # We created a method in the class. This method gives info about the person. The "self" parameter is a reference to the current instance of the class.
        print(f"{self.name} is a {self.occ} and has a networth of {self.net}")   # slef is used to access variable that belongs to that class.

a = Person()              # We created an object "a" using class "Person"
print(a.name)
a.info()                  
a.name = "Aditya"
print(a.name)
a.info()                  # as we provided name Aditya to object a , so now self in a.info() will refer to name of object of a , that is aditya