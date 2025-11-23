import random
x=True
l=3
print('Welcome to the Guessing Game\n')
print('You have three lives.')
x=str(random.randint(0,10))
print('A random number between 0 and 10 (could be 0 or 10) has been selected')
while x:
   y=input('Please enter your guess:  ')
   if x==y:
        print('You are correct.\nYou Win')
        break
   if l==1:
        print('You have lost all of your lives.')
        print('You lose.')
        break
   if y!=x:
       l=l-1
       print('Oops! That\'s not right.')
       print('You have',l,'lives left.')


