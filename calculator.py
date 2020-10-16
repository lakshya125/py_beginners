

#######################################################################################
#Initialisation of variables
#######################################################################################
k=1
a=b=0

#######################################################################################
#Functions made for specific Mathematical tasks
#######################################################################################
def add(a,b):
    return(a+b)
def substract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)

#######################################################################################
#Function for taking input from the user and checking the validity of the input
#######################################################################################
def Input(n):
    try:
        a = int(input("Enter the value of first number :- "))
        b = int(input("Enter the value of Second number :- "))
        if(n==1):
            print("The sum is " ,add(a,b))
        elif(n==2):
            print("The Substraction is ",substract(a,b))
        elif(n==3):
            print("The multiplication is ",multiply(a,b))
    except ValueError:
        print("Error :- Invalid Input\n")
        k = int(input("Do you want to continue?\n0 for No\n1 for Yes\n"))
        if(k==0):
            print("Exiting...")
            exit(0)
        elif(k==1):
            print("Enter the Values Again")
            Input(n)

def InputDiv():
    try:
        a = int(input("Enter the value of first number :- "))
        b = int(input("Enter the value of Second number :- "))
        if(b==0):
            raise ValueError
        print("The division is ",divide(a,b))
    except ValueError:
        print("Enter a valid number .\nEx:-Second number can't be zero\n ")
        print("Exiting...")
        exit(0)

#######################################################################################
#Calling the functions to perform specific tasks and getting inputs from the user
#######################################################################################
while k:
    try:
        n = int(input("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n\nEnter your choice :- \n"))
    except ValueError:
        print("Invalid Input!\n")
        print("Exiting...")
        exit(0)

    if(n<=3):
        Input(n)
    elif(n==4):
        InputDiv()
    else:
        print("\nEnter a valid option!\n")
    k=int(input("Do you want to continue?\n0. for No\n1. for Yes\n"))
    if(k==0):
        print("Task Done.")
