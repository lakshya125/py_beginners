# recursively print out nth term of the fibonacci series
# assuming that the 0th term is 0 

n = int(input("Enter n: "))

def fib(n):
	if n <= 0:
		return 0
	elif n <= 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

print(fib(n))
