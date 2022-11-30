"To write a python program merge sort"

def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        print(mid)
        L=arr[:mid]
        R=arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1


list1=list(map(int,input().split()))
print("Given array is: ",end=" ")
print(list1)
mergeSort(list1)
print("Sorted array is: ",end=" ")
print(list1)