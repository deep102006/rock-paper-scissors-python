import random

options = ["ROCK", "PAPER", "SCISSOR"]

print("Do you want to start the game?")
choice = input("Y/N: ").upper()

if choice == "N":
    print("Thank You!! Game Closed.")

while choice == "Y":
    
    print("\nROCK, PAPER, SCISSOR!!!")
    user_move = input("Enter Your Move: ").upper()

    if user_move not in options:
        print("Please enter only ROCK, PAPER, or SCISSOR!")
        continue

    computer_move = random.choice(options)
    print("Computer chose:", computer_move)

    if computer_move == user_move:
        print("It's a TIE!")
    elif (
        (user_move == "ROCK" and computer_move == "SCISSOR") or
        (user_move == "PAPER" and computer_move == "ROCK") or
        (user_move == "SCISSOR" and computer_move == "PAPER")
    ):
        print("You WIN!! 🎉")
    else:
        print("You LOSE!! 😢")

    choice = input("\nDo you want to play again? (Y/N): ").upper()

print("Thanks for playing! ❤️")
