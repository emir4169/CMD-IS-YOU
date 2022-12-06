from os import *
import os
from time import *
import time


action = ""
player_x = int(0)


def controls(level, player_x):
    if action.lower() == "w":
        if level[player_x+1] == 0:
            level[player_x], level[player_x+1] = 0, "cmd"
            return player_x + 1
        else:
            print("Cant move player: Text in way. If you know how to make the player not eat the text for some reason make a pull request")
            return player_x
    if action.lower() == "s":
        if level[player_x-1] == 0:
            level[player_x], level[player_x-1] = 0, "cmd"
            return player_x - 1
        else:
            print("Cant move player: Text in way. If you know how to make the player not eat the text for some reason make a pull request")
            return player_x


level = [
    "cmd", 0, 0, 0, "cmd", "is", "you", 0, 0, 0, 0, 0
]


def clear_stdout():
    if os.name == 'nt': # windows
        os.system('cls')
    else:
        os.system('clear') # linux or mac
        

# Print Loop
while True:
    # Print level
    clear_stdout()
    print(level)
    # Ask for input
    action = input("Action:")
    # Update the level
    player_x = controls(level, player_x)
    # Exit if player wants to exit
    if (action.upper() == "EXIT"):
        break
    # Tick delay
    time.sleep(0.5)