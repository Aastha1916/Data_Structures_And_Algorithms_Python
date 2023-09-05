# To find the odd numbers from a given list :

nums = [1, 34, 23, 56, 89, 44, 92]
odd_nums = [num for num in nums if num % 2 != 0]
print(odd_nums)

# Using the filter function :

def find_odd(x):
    if x % 2 != 0:
        return x
nums = [1, 34, 23, 56, 89, 44, 92]
odds = list(filter(find_odd, nums))
print(odds)

# Using lambda with filter:

nums = [1, 34, 23, 56, 89, 44, 92]
odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)


# code without using map, filter and lambda
 
# Find the number which are odd in the list and multiply them by 5 and create a new list
x = [2, 3, 4, 5, 6]
y = []
for v in x:
    if v % 2:
        y += [v*5]
print(y)


# Code with map, filter and lambda

x = [2, 3, 4, 5, 6]
y = list(map(lambda v: v * 5, filter(lambda u: u % 2, x)))
print(y)