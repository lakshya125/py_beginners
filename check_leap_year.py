# Program to check whether a given year is a leap year or not

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# Taking input
num = int(input())

# Checking if a input year is leap year or not
if(is_leap_year(num)):
    print(str(num) + ' is a leap year')
else:
    print(str(num) + ' is not a leap year')
