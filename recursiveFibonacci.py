#Python programme to print fibonacci number recursively
def fibo(n):
    if n <= 1:
      return n
    else:
      return fibo(n-1) + fibo(n-2)

n = int(input("Enter the term to be printed:"))

if n == 1:
    print(0)
else: 
    print(fibo(n-1))