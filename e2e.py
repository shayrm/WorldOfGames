"""
# e2e.py

This file will have two functions.

Functions
  1. test_scores_service - it’s purpose is to test our web service. It will get the application
    URL as an input, open a browser to that URL, select the score element in our web page,
    check that it is a number between 1 to 1000 and return a boolean value if it’s true or not.

  2. main_function to call our tests function. The main function will return -1 as an OS exit
    code if the tests failed and 0 if they passed.
    
"""
from selenium import webdriver

import Utils
import os

def test_scores_service(app_url, element_id):
  # Open a web browser and navigate to a webpage
  driver = webdriver.Chrome()
  driver.get(app_url)

  # Find an element with the ID "element-id"
  element = driver.find_element_by_id(element_id)
  element_value = element.text()
  print(f"Got element value for score = {element_value}")
  

def main():
  app_url = Utils.HOME_URL
  element_id = Utils.ELEMENT_ID_SCORE
  test_result = test_scores_service(app_url, element_id)

if __name__ == "__main__":
  main()  