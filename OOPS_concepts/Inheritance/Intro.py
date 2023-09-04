# # A Python program to demonstrate inheritance

# class Person(object):
 
#     # Constructor
#     def __init__(self, name):
#         self.name = name
 
#     # To get name
#     def getName(self):
#         return self.name
 
#     # To check if this person is an employee
#     def isEmployee(self):
#         return False
 
# # Inherited or Subclass (Note Person in bracket)
# class Employee(Person):
 
#     # Here we return true
#     def isEmployee(self):
#         return True
 
# # Driver code
# emp = Person("Geek1")  # An Object of Person
# print(emp.getName(), emp.isEmployee())
 
# emp = Employee("Geek2")  # An Object of Employee
# print(emp.getName(), emp.isEmployee())

#--------------------------------------------------------------------------------------------
# Python program to demonstrate error if we forget to invoke __init__() of the parent
# But we can use the parent class method's in the child class(in which the use of instance variable is not required)

class A:
    def __init__(self, n='Rahul'):
        self.name = n
    def display(self):
      print("parent class")
 
class B(A):
    def __init__(self, roll):
        self.roll = roll
 
object = B(23)
# print(object.name) # to access parent class's instance variable
object.display() # to access parent class's method

#------------------------------------------------------------------------------------------------


# parent class
# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
 
#   def display(self):
#     print(self.name, self.age)
 
# # child class
# class Student(Person):
#   def __init__(self, name, age, dob):
#     self.sName = name
#     self.sAge = age
#     self.dob = dob
#     # inheriting the properties of parent class
#     super().__init__("Rahul", age)
 
#   def displayInfo(self):
#     print(self.sName, self.sAge, self.dob)
 
 
# obj = Student("Mayank", 23, "16-03-2000")
# obj.display()
# obj.displayInfo()