import random
print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Player, make your move: ").lower()
# print("****NO CHEATING***\n\n" * 20 )
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays {computer}")

if player == computer:
    print("It's a tie!!")
elif player == "rock":
    if computer == "scissors":
        print("Player Wins!!")
    elif computer == "paper":
        print("Computer Wins")
elif player == "paper":
    if computer == "scissors":
        print("Computer Wins!!")
    elif computer == "rock":
        print("Player Wins!!")
elif player == "scissors":
    if computer == "rock":
        print("Computer Wins!!")
    elif computer == "paper":
        print("Player Wins!!")
else:
    print("Something went wrong.")

    #allyourbasearebelongtosus