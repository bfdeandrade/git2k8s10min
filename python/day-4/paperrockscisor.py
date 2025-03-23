print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.")
player = int(input())
import random
computer = random.randint(0, 2)
if player == 0:
    if computer == 0:
        print("It's a draw.")
    elif computer == 1:
        print("You lose.")
    else:
        print("You win.")
elif player == 1:
    if computer == 0:
        print("You win.")
    elif computer == 1:
        print("It's a draw.")
    else:
        print("You lose.")
else:
    if computer == 0:
        print("You lose.")
    elif computer == 1:
        print("You win.")
    else:
        print("It's a draw.")
print(f"Computer chose {computer}.")
