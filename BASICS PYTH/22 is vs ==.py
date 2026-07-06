# is and == both are comparison operators 
# is compares exact location of object in memory / or it compares identity of two objects.
# == comapres value of the object

a,b = 4,"4"
print(a==b)
print(a is b) 
# Both will print false as a is int and b is str

a,b = 4 ,4
print(a==b)
print(a is b)
# both will print true as 4 is a constant value and it won't change, so identity of a,b is same or we can say that a,b have same memory address as 4 is constant
a,b = [1,2,3],[1,2,3]
print(a==b)
print(a is b)
# This will print true for a==b as both are equal but false for a is b because , list is immutable so python sees a,b as different object

a,b = (1,2,3),(1,2,3)
print(a==b)
print(a is b)
# This will print true for both as tuple is immutable so python interprate it as a,b is same object and a,b is equal.


# ---------------- Tuple unpacking --------------------------

x, y, z = 1, 3, 4
# This is called multiple assignment (or tuple unpacking).
# Python first creates the values (1,3,4)
# Then unpacks them into the variables : 
x = 1
y = 3
z = 4