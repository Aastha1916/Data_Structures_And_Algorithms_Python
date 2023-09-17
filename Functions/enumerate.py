l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print ("Return type:", type(obj1))
print (list(enumerate(l1)))
 
# changing start index to 2 from 0
print (list(enumerate(s1, 2)))

# Accessing the Next Element : Each time the next() is called, the internal pointer of the enumerate object 
# moves to the next element, returning the corresponding tuple of index and value.

fruits = ['apple', 'banana', 'cherry']
enum_fruits = enumerate(fruits)
 
next_element = next(enum_fruits)
print(f"Next Element: {next_element}")