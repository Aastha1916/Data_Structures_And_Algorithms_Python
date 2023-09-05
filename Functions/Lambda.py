# let us consider a function to square a number

def square(n):
    return n ** 2
print(square(5))

# using lambda we can make it pythonic

square = lambda n: n ** 2
# The expression n ** 2 gets evaluated first, and a value gets returned to the identifier square.
# The identifier square can now act as a function, and thus we can pass any number as an argument to find 
# the square of a number.
print(square(5))


# We can also extend the lambda functions by adding conditional statements : 

maxi = lambda x, y: x if x > y else y
print(maxi(4, 6))

# It can have multiple argumnets: 

# first parentheses contains a lambda form and second parentheses represents calling lambda
print( (lambda x: x**2)(5))
 
# Make function of two arguments that return their product
print ((lambda x, y: x*y)(3, 4))


# It is also often used to create function wrappers, such as Python’s decorators :
def transform(n):
    return lambda x: x + n
f = transform(3)
print(f(4))

