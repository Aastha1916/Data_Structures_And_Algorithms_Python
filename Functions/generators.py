# A simple generator for Fibonacci Numbers
def fib(limit):
      
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
  
# Create a generator object
x = fib(5)
  
# Iterating over the generator object using next
# In Python 3, __next__()
print(next(x)) 
print(next(x))
print(next(x))
print(next(x))
print(next(x))
  
# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5): 
    print(i)


#------------------------------------------------------------------------------------------

# generator expression
generator_exp = (i * 5 for i in range(5) if i%2==0)
# print(type(generator_exp))
  
for i in generator_exp:
    print(i)