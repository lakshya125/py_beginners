# Program to find xor of first n natural numbers

# Taking input
n = int(input())

if n % 4 == 0:
    print(n)
elif n % 4 == 1:
    print('1')
elif n % 4 == 2:
    print(n + 1)
else:
    print('0')
