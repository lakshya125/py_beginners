def bubble_sort(arr):
    swap = True
    idxOfLastUnsortedEle = len(arr)-1
    while swap:
        swap = False
        for i in range(0,idxOfLastUnsortedEle):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swap = True
        idxOfLastUnsortedEle -= 1
    return arr

# testing
A = [1,7,9,4,6,5,2,0,85,42,75,69,94,38,3]
print(*bubble_sort(A))
