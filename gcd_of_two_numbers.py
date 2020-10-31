# Program to find GCD of two numbers

# Method to find GCD of two numbers
def gcd(a,b):
    if b == 0: 
        return a
   
    return gcd(b,a % b)

# Taking input of two numbers i.e. a and b
a,b = list(map(int,input().split(' ')))

# Getting their GCD
gcd_of_two_numbers = gcd(max(a,b),min(a,b))

# Printing the GCD of a and b
print(gcd_of_two_numbers)
