# Program to print all the prime factors of a number

prime_factors = []

def get_all_prime_factors(num):
    itr = 2
    
    while itr * itr <= num:
        if num % itr == 0:
            prime_factors.append(itr)
            while num % itr == 0:
                num //= itr
        itr = itr + 1
    
    if num >= 2:
        prime_factors.append(num)
    

# Taking input of number
num = int(input())

get_all_prime_factors(num)

# Printing all the prime factors of number
for number in prime_factors:
    print(number, end = " ")
