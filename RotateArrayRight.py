def rightRotateArray(arr, d):
    result = [0]*(len(arr))
    for i in range(len(arr)):
        result[(i + d) % len(arr)] = arr[i]
    return result

if __name__=="__main__":
    arr = [2,1,2,3,4]
    arr = rightRotateArray(arr, 1)
    print(arr)