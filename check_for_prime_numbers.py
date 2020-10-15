print("Enter the number: ")
number = input()

is_prime = True

for i in range(2,number):
	print(number)
	if (number % i) == 0:
		is_prime = False

if number <= 1:
	is_prime = False

print(is_prime)

if is_prime:
	print(number,"is a prime number")
else:
	print(number,"is not a prime number")
