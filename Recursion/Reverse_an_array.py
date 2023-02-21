#METHOD 1 : USING TWO POINTERS
arr = list(map(int,input().split()))
def reverse(arr,l,r):
    if l==r:
        return 
    arr[l],arr[r] = arr[r],arr[l]
    reverse(arr,l+1,r-1)
reverse(arr,0,len(arr)-1)
print(arr)


#METHOD 2: USING SINGLE POINTER

arr = list(map(int,input().split()))
n = len(arr)
def reverse(arr,l):
    if l >= n//2:
        return 
    arr[l],arr[n-l-1] = arr[n-l-1],arr[l]
    reverse(arr,l+1)
reverse(arr,0)
print(arr)