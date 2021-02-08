import random

userGuess = 0
counter = 0
a = random.randint(1, 9)

while userGuess != a:
    userGuess = input("What's your guess: ")

    if userGuess == "exit":
        break

    userGuess = int(userGuess)
    counter = counter + 1

    if userGuess < a:
        print("Too low")
    elif userGuess > a:
        print("Too high")
    else:
        print("You guessed it correctly")
        print("It took you:", counter, "tries")
