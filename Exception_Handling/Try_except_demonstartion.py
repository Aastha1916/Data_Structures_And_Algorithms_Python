try:
    k = 5//0  # raises divide by zero exception.
    print(k)

except ZeroDivisionError:
    print("Can't divide by zero")

except NameError:
    print("NameError Occurred and Handled")

else:
    # this block is executed when no exception generation occurs.
    print("all ok!!")

finally:
    # this block is always executed regardless of exception generation.
    print('This is always executed')
