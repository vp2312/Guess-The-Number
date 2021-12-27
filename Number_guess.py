from random import *
print("Enter Numbers You Want to GUESS BETWEEN")
n1= int(input("ENTER THE LOWER BOUND- "))
n2= int(input("ENTER THE UPPER BOUND- "))
num = randint(n1,n2)
high=n2+1
low=n1-1
guess=0
h=0
m=0
while (guess!=num):
    
    guess= int(input("Give it a guess-\t"))
    if (guess>num):
        print("Your Guess is on a higher Side")
        high=min(high,guess)
        h=1
    elif (guess<num):
        low=max(low,guess)
        print("Your Guess is on a Lower Side")
        m=1
    else:
        h=0
        m=0
        print("Your Guessed it Right")
    
    if (h!=0):
        print(r'MINIMUM HIGHER GUESS IS {}'.format(high))
    if (m!=0):
        print(r'MAXIMUM LOWER GUESS IS {}'.format(low)