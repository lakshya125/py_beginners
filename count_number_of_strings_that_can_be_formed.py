#Count number of strings that can be formed using a,b,c with at most one ‘b’ and two ‘c’s allowed, where n is the total number of characters in a string.
def countStr(n): 
    return (1 + (n * 2) + (n * ((n * n) - 1) // 2)) 
n = int(input("Total number of characters "))
print(countStr(n)) 
