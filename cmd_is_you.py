from os import *
import os
from time import *
import time


action = ""
player_x = int(0)


def controls(map, player_x):
    player_xmore = player_x+1
    player_xless = player_x-1
    if action.lower() == "w":
        if map[player_x+1] == 0:
            map[player_x], map[player_x+1] = 0, "cmd"
            return player_x + 1
        else:
            print("Cant move player: Text in way. If you know how to fix this please make a pull request.")
            return player_x
    if action.lower() == "s":
        if map[player_x-1] == 0:
            map[player_x], map[player_x-1] = 0, "cmd"
            return player_x - 1
        else:
            print("Cant move player: Text in way. If you know how to fix this please make a pull request.")
            return player_x


level = [
    "cmd", 0, 0, 0, "cmd", "is", "you", 0, 0, 0, 0, 0
]
start_points_level = [
    "cmd", 0, 0, 0, "cmd", "is", "you", 0, 0, 0, 0, 0
]



def clear_stdout():
    if os.name == 'nt': # windows
        os.system('cls')
    else:
        os.system('clear')
        

# Print Loop
while True:
    clear_stdout()
    print("(DEBUG) os.name =" + " " + os.name)
    print(level)
    action = input("Action:")
    player_x = controls(level, player_x)
    if (action.upper() == "EXIT"):
        break
    time.sleep(0.5)