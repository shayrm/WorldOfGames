"""
This file will contain general information and operations we need
for our game.
  1. SCORES_FILE_NAME - A string representing a file name. By default “Scores.txt”
  2. BAD_RETURN_CODE - A number representing a bad return code for a function.
  3. Screen_cleaner - A function to clear the screen (useful when playing memory game or
before a new game starts).

"""

import os

# Globals
SCORES_FILE_NAME="scores.txt"
USER_NAME="Shay"
BAD_RETURN_CODE=0

def screen_cleaner():
  # Clearing the Screen
  os.system('cls')

