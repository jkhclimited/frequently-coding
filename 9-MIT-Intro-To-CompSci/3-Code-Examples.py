# an_letters = "aefhilmnorsxAEFHILMNORSX"

# word = input("I will cheer for you! Enter a word: ")
# times = int(input("Enthusiasm level (1-10): "))

# for char in word:
#     if char in an_letters:
#         print("Give me an " + char + "! " + char)
#     else:
#         print("Give me a " + char + "! " + char)
# print("What does that spell?")
# for i in range(times):
#     print(word, "!!!")

str1 = "mit u rock"
str2 = "i rule mit"
if len(str1) == len(str2):
    for char1 in str1:
        for char2 in str2:
            if char1 == char2:
                print("common letter: " + char1)
                break
# a for loop inside a for loop to check

cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)

# Bisection example
cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print ('num_guesses =' + str(num_guesses))
print (str(guess), 'is close to the cube root of' + str(cube))