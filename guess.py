# This is a game.
# Guess the number.

import random

number = random.randint(1, 11)
print('Welcome!\nThis is a guess game.\nI am thinking of a number bettween 1 and 10. ')

# Ask the user to guess 5 times.
for guessesTaken in range(1, 4):  # (!) Try setting this to 1 to 100
    print('Take a guess.')
    guess = int(input())

    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('your guess is too high')
    else:
        print('Good job! You guessed my number in ' +
              str(guessesTaken) + ' guesses!')
        break  # This condition is correct guess!

if guess != number:
    print('Nope. The number I was thinking was ' + str(number))

