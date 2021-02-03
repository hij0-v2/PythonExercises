def second_exercise_with_extras():
    user_input = int(input("Enter number: "))
    if user_input % 4 == 0:
        print("Multiplication out of 4 is possible")
    elif user_input % 2 == 0:
        print("Even")
    else:
        print("Odd")

def extras2nd_part():
    user_input1 = int(input("First number: "))
    user_input2 = int(input("First number: "))

    if user_input1 % user_input2 == 0:
        print("First number divides evenly from second number")
    else:
        print("Doesn't divide evenly")

extras2nd_part()