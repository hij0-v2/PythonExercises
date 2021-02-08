def reverse_sentence():
    user_input = input("Type your sentence here: ")
    rvr_input = user_input.split()

    print("This is your sentence backwards:", " ".join(rvr_input[::-1]))


reverse_sentence()

