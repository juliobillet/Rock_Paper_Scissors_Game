import random
import os
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# rock = 0, paper = 1, scissors = 2

rps_options = [rock, paper , scissors]

print("Welcome to the Rock Paper Scissors Game!")
players_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n")

# Start verifying if the player typed a valid number, and if so, print the corresponding ASCII Art:
if players_choice.count(".") == True:
  print("Invalid option.\nPlease restart the game and choose a valid option!\nThe options are: 0 for Rock, 1 for Paper or 2 for Scissors.")
  sys.exit()

if int(players_choice) >= len(rps_options) or int(players_choice) < 0:
  print("Invalid option.\nPlease restart the game and choose a valid option!\nThe options are: 0 for Rock, 1 for Paper or 2 for Scissors.")
  sys.exit()
else:
  print(rps_options[int(players_choice)])

# Start of the logic to make the computer choose a random option and then compare the player's choice to the computer's choice and evaluate who is going to win.
possible_options = [0, 1, 2]
computer_choice = random.choice(possible_options)
print(f"Computer's choice:\n{rps_options[computer_choice]}")

players_choice = int(players_choice)

if players_choice == computer_choice:
  print("It was a tie!")
elif players_choice - computer_choice == -1 or players_choice - computer_choice == 2:
  print("You lose!")
elif players_choice - computer_choice == -2 or players_choice - computer_choice == 1:
  print("You Win!")
