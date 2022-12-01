'''ABC is a class present in abc module and abstractmethod is a HOF

To implement a class as abstract class:
1-> a class should be inherited from ABC class i.e. make that class as child class of ABC (which act as parent class now)
2-> also we need to define a method inside that class, which will known as abstract method. So we need to decorate that method 
using abstractmethod

** An object of abstract class cannot be created i.e. Can't instantiate abstract class A with abstract method method

'''

from abc import ABC ,abstractmethod

class A(ABC):
    @abstractmethod
    def method(Self):
        pass
    def method1(self):
        pass

class B(A):
    def method2(self):
        print("i am a normal method in class B")

class C(B):
    def method(self):
        print("i am a normal method in class C")
    
#obj = C()
obj = C() #Even if the Parent Class B of child class C had not define the abstract method in class B but class C has implemented then aslo
          #object canbe created
obj.method() 
#To instantiate child class B of a abstract class A, we need to define all abstract methods of abstract class A in this class B
#normal methods of the abstract class are not mandtory to be present in the child class

# obj = A() An object of abstract class cannot be created