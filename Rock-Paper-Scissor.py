######----------------This Game is coded by RohanTheProgrammer in python Language----------------######
import random

###----------saving user's move---------###
while True:
    user_input = int(input('Choose your move (press any no. between 1-3)  \n1.Rock  \n2.Paper  \n3.Scissors  \n'))
    if user_input == 1:
        user_move = '  Rock  '
        break
    elif user_input == 2:
        user_move = '  Paper '
        break
    elif user_input == 3:
        user_move = ' Scissor'
        break
    else:
        continue

###----------options for computer to choose from---------###
computer_move_opt = [
    '  Rock  ',
    '  Paper ',
    ' Scissor'
]

comp_move = random.choice(computer_move_opt)

###----------Determinig who won or who lose---------###
def winLose():
    global result_user
    global result_comp

    if comp_move == user_move:
        result_user = result_comp = 'Draw'
    elif comp_move == '  Rock  ' and  user_move == '  Paper ':
        result_user = ' WIN'
        result_comp = 'LOSE'
    elif comp_move == '  Rock  ' and  user_move == ' Scissor':
        result_user = 'LOSE'
        result_comp = ' WIN'
    elif comp_move == '  Paper ' and  user_move == '  Rock  ':
        result_user = 'LOSE'
        result_comp = ' WIN'
    elif comp_move == '  Paper ' and  user_move == ' Scissor':
        result_user = 'WIN'
        result_comp = 'LOSE'
    elif comp_move == ' Scissor' and  user_move == '  Rock  ':
        result_user = 'WIN'
        result_comp = 'LOSE'
    elif comp_move == ' Scissor' and  user_move == '  Paper ':
        result_user = 'LOSE'
        result_comp = ' WIN'

###----------putting the result on the screen---------###
def result():
    global result_comp
    global result_user

    print('\n')
    print('\n')
    print(' ____________ ____________')
    print('|  computer  |     you    |')
    print(' ____________|____________')
    print('|  '+ comp_move +'  |  '+ user_move +'  |')
    print('|    '+ result_comp +'    |    '+ result_user +'    |')
    print('|____________|____________|')

winLose()
result()
