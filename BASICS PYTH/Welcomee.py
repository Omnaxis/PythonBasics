name = "Shashwat Singh"

def welcome(n):
    print(f"Welcome {n} happy to see you here!")

print("imported from", __name__)             # __name__ is a built-in variable in Python that represents the name of the current module. When a module is run directly, __name__ is set to "__main__". When it is imported, __name__ is set to the module's name.
# print(__name__) will print __main__ if it is run directly here. When it will be imported as a module it will print the module's name which is Welcomee in this case.

if __name__== "__main__":   # it checkes if the current file is being run directly or bing imported as a module 
    welcome(name)           # if file is run directly then this line will be executed else it will not be executed

# We generally use this if __name__== "__main__": block to write code that should only be executed when the file is run directly, and not when it is imported as a module. 
# This allows us to create reusable modules that can be imported into other scripts without executing the code in the if block.