def prime_factors(num):
    '''This function returns a list of prime factors of a given number'''
    # empty list to store the prime factors
    fact=[];
    if num<1:
        raise Exception('Enter a positive number!')
    else:
        # appending number of 2's which divides n
        while num%2==0:
            fact.append(2);
            num /=2
        i=3
        # starting from 3 checking all the odd primes that can divide n
        # iterating until n is less than square of i-1
        while i<int(num**(1/2))+1:
            while num%i==0:
                fact.append(i)
                num /=i
            i +=2
        # appending remaining n value except 1
        if num>1: fact.append(int(num))
    return fact;

try:       
    num = int(input("Enter number: "))
    print(f'Prime factors of {num}: ',prime_factors(num))
except ValueError:
    print("Invalid Input!")
except Exception as e:
    print(e)
