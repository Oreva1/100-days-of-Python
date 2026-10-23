# Project Day 4    
# Rock beat Scissors
# Scissors beat Paper
# Paper beat Rock

import random

num_list = [0, 1, 2]
computer_choice = random.randint(0,2)
print("Rule of the Game:\nRock beats Scissors\nScissors beats Paper\nPaper beats Rock\n")
human_choice = input("What do you choose? 0 for Rock, 1 for Scissors, 2 for Paper?\n")
def choice(number):
    if number == 0:
        return "Rock"
    elif number == 1:
        return "Scissors"
    elif number == 2:
        return "Paper"
    else:
        return "Wrong Choice"

if human_choice != "0" and human_choice != "1" and human_choice != "2":
    print("\nWarning: Provide one number (0 or 1 or 2)")
else:
    human_choice = int(human_choice)

    print(f"\nYou chose: {choice(human_choice)}\nComputer chose: {choice(computer_choice)}\n")

    if (human_choice == 0 and computer_choice == 1)\
        or (human_choice == 1 and computer_choice == 2)\
        or human_choice == 2 and computer_choice == 0:
            print("Result: Yayyy! You Win!")
    elif human_choice == computer_choice:
        print("Result: It's a Draw. Try again!")
    else:
        print("Result: You Lose! Try again!")