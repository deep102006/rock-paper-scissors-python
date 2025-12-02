import random

s = ["ROCK", "PAPER", "SCISSOR"]

print("Do you want to start the game?")
a1 = input("Y/N: ").upper()

if a1 == "N":
    print("Thank You!!")

while a1 == "Y":

    n = random.randint(0, 2)   # Index-based random logic (your original idea)
    computer_move = s[n]

    print("\nROCK, PAPER, SCISSOR!!!")
    m = input("Enter Your Move: ").upper()

    if m not in s:
        print("Please Enter ROCK, PAPER, or SCISSOR only!")
        continue

    print("Computer chose:", computer_move)

    if computer_move == "ROCK":
        if m == "PAPER":
            print("You win!!")
        elif m == "SCISSOR":
            print("You Lose!!")
        else:
            print("TIE")

    elif computer_move == "PAPER":
        if m == "ROCK":
            print("You Lose!!")
        elif m == "SCISSOR":
            print("You Win!!")
        else:
            print("TIE")

    elif computer_move == "SCISSOR":
        if m == "ROCK":
            print("You win!!")
        elif m == "PAPER":
            print("You Lose!!")
        else:
            print("TIE")

    a1 = input("\nDo You Want to play Again?? (Y/N): ").upper()

print("Thanks for playing! ❤️")
