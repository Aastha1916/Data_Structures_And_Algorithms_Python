'''
Methods to invoke properties of parent in child class:
1-> by super function() e.g super.abstractmethod() and
2-> by parent name by passing self in the abstract function e.g parentname.abstractmethod(self)
'''

class Parent:
    def __init__(self):
        self._num=100

class child(Parent):
    def __init__(self):
        super().__init__()
        self.var=200

    def show(self):
        print(self.var)

son = child()
son.show()


