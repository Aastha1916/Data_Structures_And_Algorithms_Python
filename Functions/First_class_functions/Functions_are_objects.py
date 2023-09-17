# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()
  
print (shout('Hello'))
# This assignment doesn’t call the function. It takes the function object referenced by shout and 
# creates a second name pointing to it, yell.
yell = shout
  
print (yell('Hello'))