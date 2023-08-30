# USING MULTIPLE DISPATCH DECORATOR
 
from multipledispatch import dispatch
 
# passing two parameter
@dispatch(int, int)
def product(first, second):
    result = first*second
    print(result)

# passing three parameters 
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)
 
# you can also pass data type of any value as per requirement
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)
 
 
# calling product method with 2 arguments
product(2, 3) 
 
# calling product method with 3 arguments but all int
product(2, 3, 2) 
 
# calling product method with 3 arguments but all float
product(2.2, 3.4, 2.3)  