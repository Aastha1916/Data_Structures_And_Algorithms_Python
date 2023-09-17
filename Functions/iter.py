# Python3 code to demonstrate
# working of iter()
 
# initializing list
lis1 = [1, 2, 3, 4, 5]
 
# printing type
print("The list is of type : " + str(type(lis1)))
print(lis1)
# converting list using iter()
lis1 = iter(lis1)
 
# printing type
print("The iterator is of type : " + str(type(lis1)))
 
# using next() to print iterator values
print("Values at 1st iteration : ")
for i in range(0, 5):
    print(next(lis1))

# doesn't print this
print("Values at 2nd iteration : ")
for i in range(0, 5):
    print(next(lis1))