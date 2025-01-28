'''
DOCSTRING
Adventure Game
Author: Amy Christopherson
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''


# Welcome message and introduction
print("Welcome to the Adventure Game!")
print("Your journey begins here...")

# Ask for the player's name
player_name = input("What is your name, adventurer? ")

# Concatenate strings to create a personalized message
print("Welcome, " + player_name + "! Your journey begins now.")
# F-string: Can use brackets {} instead of + {player_name} and not have to use as many quotations

# Describe the starting area
starting_area = '''
You find yourself in a dark forest
The sound of rustling leaves fills the air
A faint path lies ahead, leading deeper into the unknown...
'''
print(starting_area)

# Ask the player for their first decision
decision = input("Do you wish to take the path? (yes or no): ")
print(decision)
