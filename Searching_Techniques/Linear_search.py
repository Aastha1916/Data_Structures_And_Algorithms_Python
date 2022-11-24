# #ITERATIVE APPROACH
# #------------------
# #Unordered Linear Search
# def Unordered_linearSearch(l,n):
#     for i in range(len(l)):
#         if l[i]==n:
#             return "element "+str(n)+" is at index: "+str(i)
#     return '-1'
        
# l=[12,34,56,23,78,11,10]
# if Unordered_linearSearch(l,23)=='-1':
#     print("Element not found!!")
# else:
#     print(Unordered_linearSearch(l,23))


# #Ordered Linear Search
# def Ordered_linearSearch(l,n):
#     for i in range(len(l)):
#         if l[i]==n:
#             return "element "+str(n)+" is at index: "+str(i)
#         elif l[i]>n:
#             return '-1'
    
        
# l=[12,14, 17, 19, 20, 22, 23]
# if Ordered_linearSearch(l,15)=='-1':
#     print("Element not found!!")
# else:
#     print(Ordered_linearSearch(l,23))


#RECURSIVE APPROACH
def linear_search(n,l,key):
    if n==len(l):
        return -1
    elif l[n]==key:
        return n
    else:
        return linear_search(n+1,l,key)
l=[12,34,56,23,78,11,10]
key = 25
ans = linear_search(0,l,key)
if ans == -1:
    print("Element not found!!")
else:
    print(f'element {key} is at index: {ans}')
