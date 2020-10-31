# program to convert a decimal number to its binary recursively

# store_bits is a list for storing binary bits of num
store_bits = []

# method which will convert the num to its binary recursively
def convert_decimal_to_binary(num):
    if num > 0:
        convert_decimal_to_binary(num // 2)
        store_bits.append(num % 2)


# To take input from the user
num = int(input("Please enter a number"))
is_negative = False

# Check if number is non-negative or not, if yes, set is_negative to True
if num < 0:
    num = -1 * num
    is_negative = True
    
# Calling convert_decimal_to_binary method 
convert_decimal_to_binary(num)

# If is_negative is True, print - in beginning acutal binary number
if is_negative == True:
    print('-',end = "")
    
# Printing the binary of num
for bit in store_bits:
    print(bit,end = "")
    
# Print 0 if num is 0 as store_bits will be empty in this case
if len(store_bits) == 0:
    print('0')

