# program to convert a decimal number to its binary iteratively

# To take input from the user
num = int(input("Please enter a number"))
is_negative = False

# Check if number is non-negative or not, if yes, set is_negative to True
if num < 0:
    num = -1 * num
    is_negative = True

# store_bits is a list for storing binary bits of num
store_bits = []

while num > 0:
    store_bits.append(num % 2)
    num //= 2
    
# Reversing the list
store_bits = store_bits[::-1]

# If is_negative is True, print - in beginning acutal binary number
if is_negative == True:
    print('-',end = "")
    
# Printing the binary of num
for bit in store_bits:
    print(bit,end = "")

# Print 0 if num is 0 as store_bits will be empty in this case
if len(store_bits) == 0:
    print('0')
