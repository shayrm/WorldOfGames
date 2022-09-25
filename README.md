# World of Games

## Live.py
Create a new python program, call it *Live.py*.

### welcome(name) 
This function has a person name as an input and returns a string in the following layout:

`Hello <name>` and welcome to the **World of Games** (WoG).\
Here you can find many cool games to play. 

### load_game() 
This function prints out the following text:\
Please choose a game to play:
 
1. Memory Game 
    - a sequence of numbers will appear for 1 second and you have to guess it back 

2. Guess Game 
    - guess a number and see if you chose like the computer 
    
3. Currency Roulette 
    - try and guess the value of a random amount of USD in ILS 


Gets an input from the user about the game he chose. \
After receiving the game number from the user, the function will get the level of difficulty \
with the following text and also save to a variable: \
`Please choose game difficulty from 1 to 5:` \

The function will check the input of the chosen game (the input suppose to be a number between 1 to 3), \
also will check the input of level of difficulty (input should be a number between 1 to 5). 

### MainGame.py 
The purpose of this file is to call the functions from Live.py, \
it can be looking as follows: 

```
from Live import load_game, welcome 

print(welcome("Guy")) 
load_game()
```

What to send me? 

A compressed zip file containing the following: 
1. MainGame.py 2. Live.py 
