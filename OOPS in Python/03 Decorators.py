# decotators allows us to modify the behaviours of functions and methods.
# we can extend functionality of a function or method without modifying its source code.
# It is a function that takes other functions as an argument and return a new function that modifies the behaviour of the original function.

def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Bye")
    return mfx

@greet
def hello():
    print("Hello Wrold")

hello()

