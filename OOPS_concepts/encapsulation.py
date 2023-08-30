# base class  
class Base1:  
    def __init__(self):  
        # the protected member  
        self._p = 78  
        ## the private member
        self.__q = "Aastha"  
  
# derived class  
class Derived1(Base1):  
    def __init__(self): 

        # now, we will call the constructor of Base class 
        # Base1.__init__(self)  
        super().__init__()
        print ("We will call the protected member of base class: ", self._p)  

        # Now, we will be modifing the protected variable:  
        self._p = 433  
        print ("we will call the modified protected member outside the class: ", self._p) 

        # Now, we will try to access private member of base class--> it will give error
        # uncomment it to see the error:
        # print("We will call the private member of base class: ",self.__q) 
 
        # to remove error using name mangling:
        print("Call encapsulated private member use name mangling : ",self._Base1__q)
  
obj_1 = Derived1()  
obj_2 = Base1()  
  
# here, we will call the protected member  
# this can be accessed but it should not be done because of convention  
print ("Access the protected member of obj_1: ", obj_1._p)  
  
# here, we will access the protected variable outside the class
print ("Access the protected member of obj_2: ", obj_2._p) 

#calling private encapsulated variable outside the class by creating object of that class
print ("Access the private member of obj_2: ", obj_2._Base1__q)

'''How to access encapsulated variable? 
--> Python's private and secured members can be accessed from outside the class using Python name mangling.'''

