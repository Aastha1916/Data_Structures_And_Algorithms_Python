'''
Methods to invoke properties of parent class in child class:
1-> by super function() e.g super.constructor() and
2-> by parent name by passing self in the abstract function e.g parentname.abstractmethod(self)
'''

class Parent:
    def __init__(self):
        self._num=100
        print("Parent class instantiated")

class child(Parent):
    def __init__(self):
        # super().__init__()
        print("Parent class constructor called ")
        Parent.__init__(self)
        print("Child class instance members instantiated")
        self.var=200

    def show(self):
        print(self.var)

son = child()
son.show()


