
#This program is to find reverse of a string - all inputs are taken from user.

# The below methods are to find reverse of a string

def reverse_slicing(s):
    return s[::-1]

def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # appending chars in reverse order
    return s1

def reverse_while_loop(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1

def reverse_join_reversed_iter(s):
    s1 = ''.join(reversed(s))
    return s1

def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)

def reverse_recursion(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0]

if __name__ == "__main__":
    # Taking inputs from user
    input_str = input("Please input a string: ")
    print('Reverse String using slicing =', reverse_slicing(input_str))
    print('Reverse String using for loop =', reverse_for_loop(input_str))
    print('Reverse String using while loop =', reverse_while_loop(input_str))
    print('Reverse String using join and reversed =', reverse_join_reversed_iter(input_str))
    print('Reverse String using list reverse =', reverse_list(input_str))
    print("Reverse String using recursion =",reverse_recursion(input_str))


