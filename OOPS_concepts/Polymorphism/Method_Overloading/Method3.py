# USING NONE
def add(a=None, b=None):
    # Checks if both parameters are available
    
    if a != None and b == None:
        print(a)
    else:
        print(a+b)
 
 
# two arguments are passed, returns addition of two
add(2, 3)

# only one argument is passed, returns a
add(2)