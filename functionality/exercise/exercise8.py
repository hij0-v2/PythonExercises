game = True

while game:
    player = input("Write rock, paper, scissors: ")
    player2 = "rock"
    tie = False

    if player == player2:
        print("Tie")
        tie = True
    elif player == "rock" or player == "Rock":
        if player2 == "paper" or player2 == "Paper":
            print("You lose")
        else:
            print("You win")
    elif player == "paper" or player == "Paper":
        if player2 == "scissors" or player2 == "Scissors":
            print("You lose")
        else:
            print("You win")
    elif player == "scissors" or player == "Scissors":
        if player2 == "rock" or player2 == "Rock":
            print("You lose")
        else:
            print("You win")
    else:
        print("Somethings wrong. Check your spelling")
        tie = True

    if not tie:
        game = False
