def hello_decorator(func):
    def inner1(*args, **kwargs):
         
        print("before Execution")
        returned_value = func(*args, **kwargs)
        print("after Execution")
        return returned_value
         
    return inner1
 
 
# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b
 
a, b = 1, 2
 
# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))