def proper_divisors(num):
    '''This function accepts a number and returns the list of proper divisors of a number.'''
    # validation for negative number
    if(num<1):
        raise Exception('Enter a positive number')
    # 0 for num=1
    if num==1:
        return 0;
    # default initialization
    divisors=[1,]
    # iterating from 2 to sq root of num
    for i in range(2,int(num**(1/2))+1):
        # divisor
        if num%i==0:
            # if both divisors are not equal
            if i != num/i:
                divisors.extend((i,int(num/i)))
            # when both are equal adding once
            else:
                divisors.append(i)
    divisors.sort()
    return divisors;

try:
    n = int(input("Enter number: "))
    # calling proper_divisors(num) method
    print(f'The list of proper divisors of {n} is: {proper_divisors(n)}')
except ValueError:
    print('Invalid input!')
except Exception as e:
    print(e)
