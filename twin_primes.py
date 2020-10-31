# method to check if number is prime
def isPrime(n):
    '''This function returns True if a given number is Prime'''
    if n>1:
        for i in range(2,n//2):
            if n%i==0:
                return False;
        return True;
    else:
        raise Exception('Number must be greater than 1!');

def twin_prime(num):
    """This function accepts a number and print all the twin primes less than that number"""
    if num<0:
        raise Exception('Enter a positive value only!')
    # assuming number to be greater than 5 as no twin primes exist below 5
    if num>=5:
        # initial value for number 3
        isCurrentPrime = True;
        # iterating over odd numbers
        for i in range (3,num-1,2):
            # validating prime for next odd using helper method isPrime()
            isNextPrime = isPrime(i+2);
            # checking twin primes
            if isCurrentPrime and isNextPrime:
                print(f'({i},{i+2})',end=", ")
            isCurrentPrime = isNextPrime
    else:
        print("No twin primes exist")
    return;

try:       
    num = int(input("Enter number: "))
    print(f'Twin primes less than {num} are:')
    twin_prime(num)
except ValueError:
    print("Invalid Input!")
except Exception as e:
    print(e)
