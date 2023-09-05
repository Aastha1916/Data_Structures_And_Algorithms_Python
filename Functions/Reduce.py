# To compute a sum of the first five integers :

nums = [1, 2, 3, 4, 5]
summ = 0
for num in nums:
    summ += num
print(summ)

# Using the reduce function :

from functools import reduce 
nums = [1, 2, 3, 4, 5]
summ = reduce(lambda x, y: x + y, nums)
print(summ)