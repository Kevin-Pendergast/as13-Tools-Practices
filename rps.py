# This game was built using GitHub Copilot, but notably the code
# matches this website's version almost identically:
#   https://realpython.com/python-rock-paper-scissors/

import random

play = True

while(play == True):

    user_action = input("Enter throw (rock, paper, scissors): ")
    ai_action = random.choice(["rock", "paper", "scissors"])

    print(f"\nYou chose {user_action}, AI chose {ai_action}.\n")

    if user_action == ai_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if ai_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if ai_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if ai_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


    question = True
    while(question == True):
        play_again = input("Would you like to play again? (yes/no): ")
        if (play_again.lower() == "yes"):
            play = True
            question = False
        elif (play_again.lower() == "no"):
            play = False
            print("Thanks for playing!")
            question= False
            exit()
        else:
            print("Invalid Input: Please answer yes or no")