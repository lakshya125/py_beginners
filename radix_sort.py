def count_sort(arr,place):
    n = len(arr)
    count = [0]*10
    result = [0]*n
    
    for i in range(n):
        idx = arr[i]//place
        count[idx%10] += 1
        
    for i in range(1,10):
        count[i] += count[i-1]
        
    i = n-1
    
    while i>=0:
        idx = arr[i] // place
        result[count[idx%10]-1] = arr[i]
        count[idx%10] -= 1
        i = i-1
        
    return result

def radix_sort(arr):
    max_ele = max(arr)
    place = 1
    
    while max_ele // place > 0:
        arr = count_sort(arr,place)
        place *= 10
        
    return arr

#testing
A = [1,7,9,4,6,5,2,0,40,75,964,784,12,155,101,320]
print(*radix_sort(A))
