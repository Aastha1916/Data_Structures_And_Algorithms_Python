def hybrid(add,a,b):
    def mul(a,b):
        add(a,b)
        print("The multiplication of given numbers",a*b)
    return mul

# @hybrid()----> Not applicable here, because parameters are to be given to the HOF 
def add(a,b):
    print("The addition of given numbers", a+b)

a=9
b=8
add = hybrid(add,a,b)
add(a,b)