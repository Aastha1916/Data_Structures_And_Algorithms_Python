# The problem with method overloading in Python is that we may overload the methods but can only use the 
# latest defined method.


def product(a, b):
	p = a * b
	print(p)

def product(a, b, c):
	p = a * b*c
	print(p)

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
product(4, 5, 5)
