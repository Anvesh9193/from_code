import random
rock=1
paper=2
scissors=3
pointu=0
pointc=0
i=0

list1=[rock,paper,scissors]

print('Welcome to rock, paper, scissors vs the computer.')

a=int(input('How many times do you wanna play?:'))

while i in range(a):
    user=int(input('Enter 1 for rock, 2 for paper and 3 for scissors:'))
    comp=random.choice(list1)

    #rock
    if user==1:
        if comp==1:
            print('Computer picked rock, no one wins.-_-')
        elif comp==2:
            print('Computer picked paper, you lose :(')
            pointc=pointc+1
        else:
            print('Computer picked scissors, you win!!!:D')
            pointu=pointu+1

    #paper
    if user==2:
        if comp==2:
            print('Computer picked paper, no one wins.-_-')
        elif comp==3:
            print('Computer picked scissors, you lose :(')
            pointc=pointc+1
        else:
            print('Computer picked rock, you win!!!:D')
            pointu=pointu+1

    #scissors
    if user==3:
        if comp==3:
            print('Computer picked scissors, no one wins.-_-')
        elif comp==1:
            print('Computer picked rock, you lose :(')
            pointc=pointc+1
        else:
            print('Computer picked paper, you win!!!:D')
            pointu=pointu+1

    i=i+1

print('You won',pointu,'time/s and you lost',pointc,'time/s.')