# User inputs number of sides on the die
# User decides to roll or not
# Active code goes inside an infinite loop

import random

# User input for number of faces on the die
sides = input('How many sides on the die? (Integers only): ')
if sides.isnumeric() == True:
    print('Press enter to roll. Input X to exit.')
    while True:
        choice = input('Press enter to roll. ')
        if choice == '':
            result = random.randint(1, int(sides))
            print(f'You rolled a {result}')
        elif choice == 'x' or choice == 'X':
            print('Thank you for playing.')
            break
else:
    print('Invalid input.')