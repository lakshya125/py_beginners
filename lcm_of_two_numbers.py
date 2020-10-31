# Program to find LCM of two numbers

# Method to find GCD of two numbers
def gcd(a,b):
    if b == 0: 
        return a
        
    if a % b == 0:
        return b
    return gcd(b,a % b)

# Taking input of two numbers i.e. a and b
a,b = list(map(int,input().split(' ')))

# Getting their GCD
gcd_of_two_numbers = gcd(max(a,b),min(a,b))

# Getting their LCM
lcm_of_two_numbers = a * b // gcd_of_two_numbers

# Printing the LCM of a and b
print(lcm_of_two_numbers)
