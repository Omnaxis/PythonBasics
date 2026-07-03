x = 10   # This is a global variable 
def my_func():
    global x  # here x will be trated as a global variable as used global keyword. Whithout it x would be treated as local varible and any change in x will not be reflected outside the function.
    x = 5

    y = 15  # This is a local variable as it is defined iside a function.
    # y can only be accessed inside this function.
    print(y)

print(x)  # this will print 10 as the value of x is 10 before calling the function.
my_func() # As we called the function, the value of x will be changed as given in function as we have specified that x in the function is global using global keyword.
print(x)  # This will print 5 as we have changed the value of x inside the function using global keyword.  
