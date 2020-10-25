'''This is an optimized method of checking if a number is prime or not. Rather than finding all factors we 
find factors till Sqaure root of the number to decrease processing.'''
import math
print("Enter the number: ")
num = int(input())
if num > 1:
   # check for factors till square root of the number - This decreases processing
   for i in range(2, int(math.sqrt(num)) + 1):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
