# A short program: guess the number
import random
secretNumber = 21
print('Guess my favorite number, it is between 1 and 100.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Try a higher number.')
    elif guess > secretNumber:
        print('Try a lower number.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Congratulations! You guessed my favorite number in ' + str(guessesTaken) + ' guesses!')
else:
    print('You have ran out of six guesses! My favorite number is ' + str(secretNumber))