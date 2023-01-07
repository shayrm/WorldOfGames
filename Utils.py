"""
This file will contain general information and operations we need
for our game.
  1. SCORES_FILE_NAME - A string representing a file name. By default “Scores.txt”
  2. BAD_RETURN_CODE - A number representing a bad return code for a function.
  3. Screen_cleaner - A function to clear the screen (useful when playing memory game or
before a new game starts).

"""
import subprocess
from time import sleep
from random import uniform
import os, platform, sys
import MainScores
from datetime import datetime
import threading

##############
# Globals
##############
MAIN_DIRECTORY = os.path.dirname(__file__)
SCORES_FILE_NAME=f"{MAIN_DIRECTORY}/scores.txt"
USER_NAME="Shay"
BAD_RETURN_CODE=0
HOST_IP="127.0.0.1"
HOST_FLASK_PORT=5000
HOME_URL=f"http://{HOST_IP}:{HOST_FLASK_PORT}/"
HOME_PATH = os.path.abspath("./")
REPLAY = True

# datetime object containing current date and time
NOW = datetime.now()
# dd/mm/YY H:M:S
DT_STRING = NOW.strftime("%d/%m/%Y %H:%M:%S")


# Generic Error message
ERROR_MSG = "No Errors"

def reset_error_msg():
  ERROR_MSG = "No Errors"
  
# WEB PAGE ELEMENT
ELEMENT_ID_SCORE="score"
def screen_cleaner():
  # Clearing the Screen
  os.system('cls')

def start_web_server():
  #web_app = f"py.exe {MAIN_DIRECTORY}\MainScores.py"
  web_app = f"{MAIN_DIRECTORY}\MainScores.py"
  print(f"\nStarting the web app from: {web_app}")
  #thr =  threading.Thread(target=MainScores.main())
  #thr.start()
  #threading.Thread(MainScores.main())
  #os.system(f"py.exe {web_app}")
  #subprocess.Popen([os.system(web_app)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  subprocess.Popen(["py.exe", web_app], stdin=None, stdout=None, stderr=None)
                   
def generic_error():
    print("Not a good selection, please enter a valid option! Try again.")
    return

def print_effect(input_line):
  for x in input_line:
    print(x, end='')
    sys.stdout.flush()
    sleep(uniform(0, 0.1))

def find_os():
  system = platform.system()
  return system

  #if system == "Windows":
  #    # code to run on Windows
  #elif system == "Linux":
  #    # code to run on Linux
  #elif system == "Darwin":
  #    # code to run on macOS
  #else:
  #    # code to run on other platforms