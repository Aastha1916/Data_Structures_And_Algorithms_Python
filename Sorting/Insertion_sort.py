# Iterative Approach

def insertsort(l):
    for i in range(1,len(l)):
        key = l[i]
        j = i-1
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j-=1
        l[j+1] = key
        # print(l)
    return l

print(insertsort([23,44,1,4,66,7]))

#-----------------------------------
# Recursive Approach

def insertsort(l,n):
    if n<=1:
        return l
    insertsort(l, n-1)
    key = l[n-1]
    j = n-2
    while j >= 0 and l[j] > key:
        l[j+1] = l[j]
        j-=1
    l[j+1] = key
    
arr=[23,44,1,4,66,7]
insertsort(arr,len(arr))
print(arr)