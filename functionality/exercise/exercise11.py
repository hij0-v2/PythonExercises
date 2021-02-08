def prime_number():
    user_input = int(input("Insert number please: "))

    if user_input % 2 != 0:
        print("Number is prime")
    else:
        print("Number is not prime")


prime_number()
