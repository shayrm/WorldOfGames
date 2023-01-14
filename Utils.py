"""
## Utills.py

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
from dotenv import load_dotenv

import os, platform, sys
import MainScores
from datetime import datetime
import threading


class Utils:
  def __init__(self) -> None:
    
    # Loading environment from .env
    load_dotenv()
    
    ##############
    # Globals
    ##############
    self.MAIN_DIRECTORY = os.path.dirname(__file__)
    self.MAIN_DIRECTORY_ENV = os.getenv("MAIN_DIRECTORY")
    self.SCORES_FILE_NAME=f"{self.MAIN_DIRECTORY}/scores.txt"
    self.SCORES_FILE_NAME_ENV = os.getenv("SCORES_FILE_NAME")
    self.USER_NAME = os.getenv("USER_NAME")
    self.BAD_RETURN_CODE=0
    self.HOST_IP="127.0.0.1"
    self.HOST_IP_ENV = os.getenv("HOST_IP")
    self.HOST_FLASK_PORT=5000
    self.HOME_URL=f"http://{self.HOST_IP}:{self.HOST_FLASK_PORT}/"
    self.HOME_PATH = os.path.abspath("./")
    self.REPLAY = True
    self.OS_NAME = self.find_os()        
    self.PLATFORM = os.getenv("PLATFORM")
    self.first_round = True
    
    # Set test to True only on lab env
    if self.PLATFORM == "lab":
      self.E2E_TEST= True
    else:
      self.E2E_TEST = False
      
    # datetime object containing current date and time
    self.NOW = datetime.now()
    # dd/mm/YY H:M:S
    self.DT_STRING = self.NOW.strftime("%d/%m/%Y %H:%M:%S")
    
    # WEB PAGE ELEMENT
    self.ELEMENT_ID_SCORE="score"
    
    
    # Generic Error message
    self.ERROR_MSG = "No Errors"
  
  ##########################
  # Support functions
  ##########################
  
  def game_options(slef):
    game_options = {
        "Guess Game": "Guess a number and see if you chose like the computer\n",
        "Memory Game": "a sequence of numbers will appear for 1 second and you have to guess it back\n",
        "Currency Roulette": "Try and guess the value of a random amount of USD in ILS\n"
    }
    return game_options
  
  # sleep for x seconds
  def time_out(self, x):
    sleep(x)
      
  def reset_error_msg(self):
    self.ERROR_MSG = "No Errors"
    
  def screen_cleaner(self):
    # Clearing the Screen
    if self.OS_NAME == "Windows":
      os.system('cls')
    else:
      os.system('clear')
    
  def start_web_server(self):
    if self.OS_NAME == "Windows":
      self.web_app = f"{self.MAIN_DIRECTORY}\MainScores.py"
      subprocess.Popen(["py.exe", self.web_app], stdin=None, stdout=None, stderr=None)
    else:
      self.web_app = f"{self.MAIN_DIRECTORY}/MainScores.py"
      subprocess.Popen(["python3", self.web_app], stdin=None, stdout=None, stderr=None)
      subprocess.check_output(['echo "check subprocess outout"'], shell=True, stderr=subprocess.STDOUT)
    
    print(f"\nStarting the web app from: {self.web_app}")
                   
  def generic_error(self):
      print("Not a good selection, please enter a valid option! Try again.")
      return
  
  def print_effect(self, input_line):
    for x in input_line:
      print(x, end='')
      sys.stdout.flush()
      if self.first_round:
        sleep(uniform(0, 0.1))
      else:
        sleep(0)
    
  def find_os(self):
    self.system = platform.system()
    return self.system
  
    #if system == "Windows":
    #    # code to run on Windows
    #elif system == "Linux":
    #    # code to run on Linux
    #elif system == "Darwin":
    #    # code to run on macOS
    #else:
    #    # code to run on other platforms

def main():
   app_env = Utils()
   return app_env

if __name__ == "__main__":
  main()