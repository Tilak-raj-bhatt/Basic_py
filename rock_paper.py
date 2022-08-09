from multiprocessing import RLock
import random

def choices_both():
    user_choice = input("Enter your choice among (rock, paper, sissors):")
    cases = ["rock", "paper", "sissors"]
    computer_choice = random.choice(cases)
    choices = {"user": user_choice, "computer": computer_choice}
    return choices

def who_win(player, computer):
    if player == computer:
        print("its a tie!!  better luck next time")
    elif player == "rock":
        if computer == "paper":
            return "papar covers the rock, and the computer wins"
        else:
            return "rock smashes the sissors, and you smashes the game"
    elif player == "paper":
        if computer == "rock":
            return "papar covers the rock, and you won the game"
        else:
            return "sissors cut the paper, and you losses the game"
    else:
        if computer == "paper":
            return "sissors cut the paper, and you won the game"
        else:
            return "rock smashes the sissors, and you lost the game"




result = choices_both()
print(f'you chose {result["user"]} and the computer chose {result["computer"]}')
print(who_win(result["user"], result["computer"]))