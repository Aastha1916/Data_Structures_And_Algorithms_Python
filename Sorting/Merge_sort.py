# "To write a python program merge sort"
def merge(l,r,mid,arr):
    s1 = l
    s2 = mid+1    
    merge_arr = []
    while s1 <= mid and s2 <= r :
        if arr[s1] <= arr[s2]:
            merge_arr.append(arr[s1])
            s1+=1
            
        else:
            merge_arr.append(arr[s2])
            s2+=1
    while s1<=mid:
        merge_arr.append(arr[s1])
        s1+=1
    while s2<=r:
        merge_arr.append(arr[s2])
        s2+=1
    for i in range(l,r+1):
        arr[i] = merge_arr[i-l]   
    

def merge_sort(l,r,arr):
    mid = (l+r)//2
    if l < r:
        merge_sort(l,mid,arr)
        merge_sort(mid+1,r,arr)
        merge(l,r,mid,arr)
  
list1=list(map(int,input().split()))
n = len(list1)
print("Given array is: ",end=" ")
print(list1)
merge_sort(0,n-1,list1)
print("Sorted array is: ",end=" ")
print(list1)




