#The program shortens fractions. The user can insert the counter and
#denominator. The program then shortens the fraction by calculating
#the greatest common divisor of the two values.

print("This program shortens fractions for you. \nAll inputs must be integers.\n")

def shortenFraction ():
    try:
        counter = int(input("Please insert the counter of your fraction >> "))
        denominator = int(input("Please insert the denominator of your fraction >> "))
    except ValueError as ve:
        print("Your input is not an integer.")
        shortenFraction() #Call the function again to allow the user to go for a new try

    c = counter
    d = denominator

    #Logic to calculate the greatest common divisor of the fraction
    if c == 0:
        gcd = d
    else:
        while d != 0:
            if c > d:
                c = c - d
            else:
                d = d - c
        gcd = c       #gcd stands for 'greatest common divisor'

    #output
    print (f"The greatest common divisor of your fraction is {gcd}.")
    c_shortened = int(counter / gcd)
    d_shortened = int(denominator / gcd)
    print (f"Shortened Fraction: {c_shortened} / {d_shortened}")

    if input("\nAgain? (y/n) >> ").lower == "y":
        shortenFraction()
    else:
        print("Program stopped.")

shortenFraction() #Call the function for the firat time
