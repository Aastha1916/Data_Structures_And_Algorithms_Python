name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
 
# using zip() to map values
mapped = zip(name, roll_no)
 
print(set(mapped))
# Unzipping Using zip() :
# unzipped_name,unzipped_roll_no = zip(*mapped)
# print("Names : ",end = "")
# print(unzipped_name)
# print("Roll No : ",end = "")
# print(unzipped_roll_no)

# Python zip() with enumerate :

names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]
 
for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)

# Python zip() with Dictionary :

stocks = ['GEEKS', 'For', 'geeks']
prices = [2175, 1127, 2750]
 
new_dict = {stocks: prices for stocks,
            prices in zip(stocks, prices)}
print(new_dict)

# Python zip() with Tuple :

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped = zip(tuple1, tuple2)
result = list(zipped)
print(result)




 