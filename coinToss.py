import random
list = ['heads', 'tails']
toss = random.choice(list)
print(toss)
guess = input('Guss the coin toss! Enter heads or tails: ')
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again')
    guesss = input()
    if toss == guesss:
        print('You got it!')
    else:
        print('Nope! You are really bad at this game.')