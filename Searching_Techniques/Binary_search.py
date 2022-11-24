#ITERATIVE APPROACH
def binarySearch1(arr, element, low, high):
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==element:
            return mid
        elif arr[mid]<element:
            low=mid+1
        else:
            high=mid-1
    return -1

arr = [2, 8, 10, 14, 18, 22]
element = 11
result = binarySearch1(arr, element, 0, len(arr)-1)
if result!=-1:
    print("element is present at index",result)
else:
    print("Element is not present in array")


#RECURSIVE APPROACH
def binarySearch(arr,l,r,x):
    if r>=1:
        mid = (r+1)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr,1,mid-1,x)
        else:
            return binarySearch(arr,mid+1,r,x)
    else:
        return -1
arr=[2,3,4,10,40,45]
x=10
result=binarySearch(arr,0,len(arr)-1,x)
if result!=-1:
    print("element is present at index",result)
else:
    print("Element is not present in array")
