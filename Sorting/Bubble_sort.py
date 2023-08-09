#Iterative Approach
def Bubble_Sort(arr, n):
    
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [22, 45, 12, 47, 22, 30, 17, 90, 56]
n = len(arr)
Bubble_Sort(arr, n)
print(arr)

#Recursive Approach
def Bubble_Sort(arr, n):
    if n <= 0:
        return 
    
    for j in range(n-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    
    Bubble_Sort(arr,n-1)
    

arr = [22, 45, 12, 47, 22, 30, 17, 90, 56]
n = len(arr)
Bubble_Sort(arr, n)
print(arr)



