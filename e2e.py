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
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from time import sleep
import Utils
import os

#### ERROR!
### Could not run the test. got PATH error for Chromdriver 
### Need to set an absolute path and fix the get_element by ID
#### 


def test_scores_service(app_url, element_id):
  # Open a web browser and navigate to a webpage
  os_type = Utils.find_os()
  
  if os_type == "Windows":
    #chrome_driver = os.path.join(Utils.HOME_PATH, "chromedriver.exe")
    chrome_driver = "C:\MyStuff\Info\DevOps_Course\WorldOfGames\chromedriver.exe"
    print(f"Current path is: {chrome_driver}")
    
  elif os_type == "Linux":
    chrome_driver = os.path.join(Utils.HOME_PATH, "chromedriver")
  else:
    print(f"OS type equal to: {os_type} and it is not supported")
    exit
      
  chrome_services = Service(chrome_driver)
  #chrome_options = Options()  
  #driver_chrome = webdriver.Chrome(service=chrome_services, options=chrome_options)
  driver_chrome = webdriver.Chrome(service=chrome_services)
  driver_chrome.get(app_url)

  # Find an element with the ID "element-id"
  element = driver_chrome.find_element_by_id(element_id)
  element_value = element.text()
  print(f"Got element value for score = {element_value}")
  sleep(15)

def main():
  app_url = Utils.HOME_URL
  element_id = Utils.ELEMENT_ID_SCORE
  test_result = test_scores_service(app_url, element_id)
  print(f" Got the latest results: {test_result}")

if __name__ == "__main__":
  main()  