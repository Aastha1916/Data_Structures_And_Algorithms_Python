
def selection(arr):
    for i in range(len(arr)-1):
        minindex=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minindex]:
                minindex=j
        arr[i],arr[minindex]=arr[minindex],arr[i]
    

arr=[23,43,67,1,44,6,78,9,0,2]
selection(arr)
print(arr)



#T(n)=T(n-1)+n------------------------------------

def selection(arr,s,n):
    if s>=n-1:
        return
    minindex=s
    for j in range(s+1,n):
        if arr[j]<arr[minindex]:
            minindex=j
    arr[s],arr[minindex]=arr[minindex],arr[s]
    selection(arr,s+1,n)

arr=[23,43,67,1,44,6,78,9,0,2]
n=len(arr)
selection(arr,0,n)
print(arr)


