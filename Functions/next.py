# define a list
l = [1, 2, 3] 
# create list_iterator
l_iter = iter(l) 
 
while True:
    # item will be "end" if iteration is complete
    item = next(l_iter, "end")
    if item == "end":
        break
    print(item)


l_iter = iter([1, 2])
 
print("Next Item:", next(l_iter))
print("Next Item:", next(l_iter))
 
# this line should raise StopIteration exception
print("Next Item:", next(l_iter))

# To use next() function in integer : create an iterator from a collection of integers or use a generator 
# function to produce integers one by one

def integer_generator():
    yield 1
    yield 2
    yield 3

iterator = integer_generator()

next_item = next(iterator)  # Retrieves the next integer (1)
next_item = next(iterator)  # Retrieves the next integer (2)
next_item = next(iterator)  # Retrieves the next integer (3)
