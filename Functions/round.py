print(round(15))
 
# for floating point
print(round(51.6))
print(round(51.5))
print(round(51.4))


# Python round() function if the Second Parameter is Present

# when the (ndigit+1)th digit is =5
print(round(2.665, 2))
 
# when the (ndigit+1)th digit is >=5
print(round(2.676, 2))
 
# when the (ndigit+1)th digit is <5
print(round(2.673, 2))

# Python round() with Negative Integers 


print(round(-3.2)) 
print(round(-4.7))
print(round(-2.5))
print(round(-2.675, 2))
print(round(-1234, -2))

# Rounding Number with Math Library in Python

import math
 
num = 3.6
rounded_num = math.floor(num) # rounds down to nearest integer
print(rounded_num) # output: 3
 
rounded_num = math.ceil(num) # rounds up to nearest integer
print(rounded_num) # output: 4

# Rounding Number with Numpy Module In Python

import numpy as np
 
arr = np.array([-2.675, -1.23456789, -3.14159265])
rounded_arr = np.round(arr, decimals=3)
 
print(rounded_arr)