
def insertsort(l):
    for i in range(len(l)):
        pos=i
        while pos>0 and l[pos]<l[pos-1]:
            l[pos],l[pos-1]=l[pos-1],l[pos] 
            pos=pos-1
    return l

print(insertsort([23,44,1,4,66,7]))

#-----------------------------------

def insertsort(l,start,n):
    if start>=n-1:
        return
    pos=start
    while pos>0 and l[pos]<l[pos-1]:
        l[pos],l[pos-1]=l[pos-1],l[pos] 
        pos=pos-1
    insertsort(l, start, n)
arr=[23,44,1,4,66,7]
insertsort(arr,0,len(arr))
print(arr)