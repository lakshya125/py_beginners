# Function to generate_AP
def generate_GP(a, r, n):
    GP_series = []
    for i in range(0,n):
        GP_series.append(float(a* pow(r,i)))
    return GP_series


print('enter test_cases')	
T = int(input())

if T<=25 and 1<=T:
    for i in range(1,T+1):
        print("enter values for case",i)
        print("enter 1st element, ratio , number of terms: ")
        a,r,n = map(int, input().split())
        
        if ((int(a)<=20) and (-20<=int(a))) and  ((int(r)<=20) and (-20<=int(r))) and  ((int(n)<=20) and (-20<=int(n))):
            GP_series = generate_GP(a, r, n)
            print("GP is -")
            print(GP_series)

            sum_GP_series =a*((1- pow(r,n))/(1-r))
            print("Sum of GP terms is -")
            print (sum_GP_series) 
        
             
        else:
            print("values out of range")
else:
    print("test case out of range")
