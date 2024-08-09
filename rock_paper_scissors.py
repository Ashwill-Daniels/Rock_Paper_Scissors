"""This is a rock paper scissors game. The user will play against the 
 computer, who will randomly pick between the three options.
"""

import random

# Randomly choose an option.
option_list = ["rock", "paper", "scissors"]

# Used to track game continuation.
keep_playing = False


def rock_paper_scissors(user, computer):
    "Determines the winner of the game by comparing the two inputs."

    if user == "rock" and computer == "scissors":
        print(f"User pick: {user} ... Computer pick: {computer} ... You win!")

    elif user == "paper" and computer == "rock":
        print(f"User pick: {user} ... Computer pick: {computer} ... You win!")

    elif user == "scissors" and computer == "paper":
        print(f"User pick: {user} ... Computer pick: {computer} ... You win!")

    elif user == computer:
        print(f"User pick: {user} ... Computer pick: {computer} ... A draw!")

    elif user == "scissors" and computer == "rock":
        print(f"User pick: {user} ... Computer pick: {computer} ... You lose!")

    elif user == "paper" and computer == "scissors":
        print(f"User pick: {user} ... Computer pick: {computer} ... You lose!")

    elif user == "rock" and computer == "paper":
        print(f"User pick: {user} ... Computer pick: {computer} ... You lose!")


print("Welcome to the Rock-Paper-Scissors game!")

# Exit if the user doesn't wish to continue.
while True:
    
    # Prompt for an input.
    while True:
        user_input = input("Please enter 'rock', 'paper', or 'scissors': \
""").lower()

        if user_input in option_list:
            break
        else:
            print("Oops! Wrong input.")

    # Get a random number.
    random_pick = random.randint(0, 2)

    # Use random number to get a random list index point.
    computer_pick = option_list[random_pick]

    # Call the game function.
    rock_paper_scissors(user_input, computer_pick)

    # Prompt for another round.
    while True:
        continue_game = input("Want to go another round?Y/N ").upper()

        if continue_game == "Y":
            keep_playing = True
            break
        elif continue_game == "N":
            keep_playing = False
            break
        else:
            print("Please enter 'Y' or 'N': ")

    # Exit the program.
    if not keep_playing:
        print("Thanks for playing my game!")
        break


