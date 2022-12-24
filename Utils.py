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
HOST_IP="127.0.0.1"
HOST_FLASK_PORT=5000
HOME_URL=f"http://{HOST_IP}:{HOST_FLASK_PORT}/"

# WEB PAGE ELEMENT
ELEMENT_ID_SCORE="score"
def screen_cleaner():
  # Clearing the Screen
  os.system('cls')

