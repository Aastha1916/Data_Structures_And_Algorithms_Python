# To find a square of the first five odd numbers :

squares = []
for n in range(1, 10, 2):
    squares.append(n ** 2)

print(squares)

# Using the map function :

def square(n):
    return n ** 2
squares = map(square, range(1, 10, 2))  
# returns map object
print(squares)
print(list(squares))


# map function can have multiple iterables. Let’s take a quick example to demonstrate the same :

num1 = [2, 4, 9]
num2 = [3, 8, 5]
result = list(map(lambda x, y: x + y, num1, num2))
print(result) # Here, we have performed element-wise addition of lists.


# Using lambda with map :
squares = list(map(lambda n: n ** 2, range(1, 10, 2)))
print(squares)