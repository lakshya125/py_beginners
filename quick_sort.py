'''Quick sort using last element as pivot in partitioning'''

def partition(arr,low,high):
    i = low-1
    for j in range(low,high):
        if arr[j]<=arr[high]:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[high],arr[i+1] = arr[i+1],arr[high]
    return i+1

def quick_sort(arr,start=None,end=None):
    if start == None:
        start = 0
    if end == None:
        end = len(arr)-1        
    if start<end:
        pivot = partition(arr,start,end)
        quick_sort(arr,start,pivot-1)
        quick_sort(arr,pivot+1,end)
    return arr

A = [1,7,9,4,6,5,2,0,85,42,75,69,94,38]
print(*quick_sort(A))
