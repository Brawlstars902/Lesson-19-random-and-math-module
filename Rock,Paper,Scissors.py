import random

print('\n\n--WELCOME TO THE ROCK, PAPER, SCISSORS GAME--\n')
while True:
    u=input('Please enter a choice, rock, paper or scissors ( no capital letters ):  ')
    a=['rock','paper','scissors']
    b=str(random.choice(a))
    if b==u:
        print('The computer chose',b,'and you chose',u,'. Play again.')
    #rock and paper
    if b=='rock'and u=='paper':
        print('The computer chose',b,'and you chose',u,'.\n--You won')
        break
    #paper and rock
    if b=='paper'and u=='rock':
        print('The computer chose',b,'and you chose',u,'.\n--You lost')
        break
    #rock and scissors
    if b=='rock'and u=='scissors':
        print('The computer chose',b,'and you chose',u,'.\n--You lost')
        break
    #scissors and rock
    if b=='scissors'and u=='rock':
        print('The computer chose',b,'and you chose',u'.\n--You won')
        break
    #paper and scissors
    if b=='paper'and u=='scissors':
        print('The computer chose',b,'and you chose',u,'.\n--You won')
        break
    #scissors and paper
    if b=='scissors'and u=='paper':
        print('The computer chose',b,'and you chose',u,'.\n--You lost')
        break
    #if u is not correct
    if u!='rock'and u!='paper'and u!='scissors':
        print('Invalid input. Try again.')
print('\nMade by Ishaan Ali')