# User inputs a guess for the number

import random

rng = random.randint(1, 100)
while True:
    try:
        guess = int(input('Guess the number between 1 and 100: '))
        if guess > rng:
            print('Too high!')
        elif guess < rng:
            print('Too low!')
        else:
            print('Congratulations!')
            break
    except ValueError:
        print('Please enter a valid number')