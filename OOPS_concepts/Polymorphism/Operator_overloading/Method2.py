# Python Program illustrate how to overload an binary + operator And how it actually works
 
class A:
    def __init__(self, a):
        self.a = a
 
    # adding two objects
    def __add__(self, o):
        return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")
 
print(ob1 + ob2)
print(ob3 + ob4)

# Actual working when Binary Operator is used.
print(A.__add__(ob1, ob2))
print(A.__add__(ob3, ob4))

#And can also be Understand as :
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))


# Python program which attempts to overload ~ operator as binary operator : throw a syntax error.

class A:
    def __init__(self, a):
        self.a = a
 
    # Overloading ~ operator, but with two operands
    def __invert__(self):
        return "This is the ~ operator, overloaded as binary operator."
 
 
ob1 = A(2)
ob2 = A(3)
print(~ob1) 
# print(ob2~ob1) # throws error
