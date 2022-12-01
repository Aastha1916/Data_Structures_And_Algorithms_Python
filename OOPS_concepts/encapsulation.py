'''How to access encapsulated variable'''

class Parent:
    def __init__(self):
        self.__num=100 #encapsulated variable

class child(Parent):
    def __init__(self):
        super().__init__()
        self.var=200

    def show(self):
        print(self._Parent__num) #calling encapsulated variable using name mangling
        print(self.var)

son = child()
son.show()
par = Parent()
print(par._Parent__num) #calling encapsulated variable outside the class by creating object of that class