import sys

__program__='G2'
def is_squa(num):
    tmp=int(pow(num,.5))
    if pow(tmp,2)==num:
        return True
    return False

def check_2(num):
    div=2
    count=0
    while div<=num :
        if num%div==0:
            num=int(num/div)
            if div%4==3:
                count+=1
        else :
            if count%2:
                # cannot be represented by 2 square
                return False

            div+=1
            count=0

    if count%2:
        if div%4==3:
            return False
    return True

def check_3(num):
    while num%4==0:
        num=int(num/4)
    if num%8==7:
        # cannot be represented by 3 square
        # by lagranges theorem definitely 4
        return False
    else :
        ## Any number other than of the form 4^n  * (8k+7)
        ## can be shown as 3 square
        ## if it is not 2 then it is 3
        return True

def min_squa_need(n):
    if is_squa(n):
        return 1
    elif check_2(n):
        return 2
    elif check_3(n):
        return 3
    else :
        return 4
    
if __name__ == '__main__':
    ln=len(sys.argv)
    if ln == 2:
        if type(int(sys.argv[1]))==type(1) :
            print(min_squa_need(int(sys.argv[1])))
        else :
            print('Integer needed')
    elif ln >= 3:
        raise TypeError(__program__,"takes exactly one argument ("+str(ln)+" given)")
    else:
        print(' Program returns minimum number of squares needed to represent a number N')
        print('Enter 0 to exit ')
        try:
            while True:
                num=eval(input('Enter your number: '))
                if num==0:
                    exit
                
                print(min_squa_need(num))
        except :
            print('Bye')


