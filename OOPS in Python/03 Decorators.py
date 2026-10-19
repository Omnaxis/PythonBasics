# decotators allows us to modify the behaviours of functions and methods.
# we can extend functionality of a function or method without modifying its source code.
# It is a function that takes other functions as an argument and return a new function that modifies the behaviour of the original function.

def greet(fx):
    def mfx():          # This is wrapper, it's just a name we give to a function that wraps another function and adds extra behavior to it.
        print("Good Morning")
        fx()
        print("Bye")
    return mfx       # we returned wrapper as greet() function must return wrapper to fulfill hello = greet(hello) condition below , else it would throw none type error.
# We returned mfx/wrapper so that decorator can be executed whenever we call hello().

@greet        # this means hello = greet(hello)
def hello():
    print("Hello Wrold")

hello()

