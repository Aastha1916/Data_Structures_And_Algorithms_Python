'''
There are 3 properties of hof(Higher Order Function):
1-> A function which take another function as parameter or argument
2-> When a function return another function
3-> When a function contains another function inside it

A decorator is a callable which implements all the properties of HOF. Its purpose is to provide 
additional functionality.
'''

#HOF
def newfun(fun):
    print("inside newfun")
    def inner():
        print("inside inner")
        fun()
        print("i am decorator fun")
    return inner

def normal():
    print("i am normal function fun")

normal = newfun(normal)
normal()


#HOF AS DECORATOR
def newfun(fun):
    def inner():
        print("i am decorator fun")
        fun()
    return inner

@newfun     #user defined decorator
def normal():
    print("i am normal function fun")

#normal = newfun(normal)
normal()


