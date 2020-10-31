#import random library
import random
rps = ['rock','paper','scissor']
you = 0
me = 0
name = input("Hello, What is your name : ")

#explain the rules of the game
print("\nWell, " + name + " Let's play a game of rock paper scissors.\ntype in rock/paper/scissor whenever you are ready.")

def assignNumToUsrChoice(userChoice) :
    if userChoice.lower() == 'rock':
        return 0
    elif userChoice.lower() == 'paper':
        return 1
    elif userChoice.lower() == 'scissor':
        return 2
    else:
        print("That's not an option\n")
        return 4

def wannaPlayAgain(m,y) :
    while True :
        print("you - " + str(y) + " || Me - " + str(m))
        again = input("Wannna go again [yes|no] : ")
        if again.lower() == 'yes' :
            game(m, y)
        elif again.lower() == 'no' :
            quit()
        else :
            print("That's not an option\n")

def game(me, you) :
    while True:
        int = random.randint(0, 2)
        userChoice = input('\nYou : ')
        c = assignNumToUsrChoice(userChoice)
        if c == 4 :
            continue
        elif c == int :
            print('Me : ' + rps[int] + '\nAgain\n')
            continue
        elif (c == 0 and int ==1) or (c == 1 and int == 2) or (c == 2 and int == 0) :
            print('Me : ' + rps[int] + '\nGotcha\n')
            me = me + 1
            wannaPlayAgain(me,you)
        else :
            print('Me : ' + rps[int] + "\nYou won!!\n")
            you = you + 1
            wannaPlayAgain(me,you)

game(me ,you)