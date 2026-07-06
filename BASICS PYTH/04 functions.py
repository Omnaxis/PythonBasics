## FUNCTION : IT IS A BLOCK OF CODE WHICH PERFOMES A SPECIFIC TASK WHENEVER IT IS CALLED
## BUILT-IN FUNCTION : THESE FUNCTIONS ARE PRECODED IN PYTHON, EX. len(), range(), type() etc.
## USER-DEFINED FUNCTIONS : THESE AR ETHE FUNCTIONS THAT USER DEFINES AS PER THEIR NEED.

# def greaterthan(a,b):                  # we defined a function named greaterthan
#     if(a>b):
#         print(a,"is greater than",b)
#     else:
#         print(b,"is greater than",a)

# greaterthan(1000,-1.1)

# def test_01(a,b):
#     pass                            # pass statement wil not do anything and the code will move foward , it is used so that no error is displayed while excueting programme and we can write code in future


def avg(a,b,c):
    return (a+b+c)/3                 # return statement returns the value of the function to a variable [here average] , whereas print just print the value when function is called for a specific argument

average = avg(12,23,43)
print(average)                       # if insted of return we write this code with print statement i would not return the value of fcn to variable, so the output would be "none " in that case


def sum_num(num1,*num):              # *num is arbitrary 
    result = num1                     # This is used to give more than two values in the function
    for i in num :
        result+= i 
        return result
r = sum_num(10,20,30)
print(r)
 
def myfcn(**name):                   # **name is used to give more than two values(can give single values also ) in the function but in the form of key value pair and it is stored in the form of dictionary.
    print(f"The first name is {name['fname']} and lst name is {name['lname']}")
myfcn(fname= "Shashwat", lname="Singh")

result = lambda a,b : a+b           # lambda is an anonymous function which can have any number of arguments but only one expression and it is used when we want to write a small function in single line
print(result(5,3))

num = [1,2,3,4,5,6,7,8,9,10]
# def is_even(n):
#     return n % 2 == 0

# result = filter(is_even, num)
# print(list(result))
result = filter(lambda x : x%2==0,num)                # This will filter out all the even numbers from the list num and return an iterator which we can convert to list to see the output
print(list(result))

l = [1,2,3,4,5,6,7,8,9]
result = map(lambda x : x**3,l)                       # This will cube all the numbers in the list l and return an iterator which we can convert to list to see the output
print(list(result))
# Map works on every item of the list and return an iterator with the modified items as per the function provided in map. It is used to apply a function to all items in an iterable (like list, tuple etc.)
# Filter is used to filter out items from an iterable based on a function that returns True or False. It returns an iterator with the items for which the function returns True.

# --------- reduce------------
# syntax : reduce(function, iterable)
# It is a part of the functools module
# It applies a function to a sequence and returns a single value.
# It apply the function to first two elements in the iterables and then applies the function to the result and the next element and so on.

from functools import reduce 
newl= int(reduce(lambda x,y : x+y, l))
print(newl)