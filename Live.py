

def welcome(name):
    print (f"Hello {name} and welcome to the World of Games (WoG).\n Here you can find many cool games to play.")

def generic_error():
    print("Not a good selection, please enter a number! Try again.")
    return

def game_level():
    while True:
        try:
            game_level = int(input("Please choose game difficulty from 1 to 5:"))
            if (game_level <= 0) or (game_level >= 6):
                generic_error()
                continue
            else:
                print(f"got the option {game_level}")
        except ValueError:
            generic_error()
            continue
        else:
            return game_level
            break
def load_game():
    message = """
    Please choose a game to play: 
    1. Memory Game 
        - a sequence of numbers will appear for 1 second and you have to guess it back 
    
    2. Guess Game 
        - guess a number and see if you chose like the computer 
    
    3. Currency Roulette 
        - try and guess the value of a random amount of USD in ILS 

    """

    print(message)

    while True:
        try:
            user_choice = int(input("Please enter your choice:"))
            if (user_choice <=0) or (user_choice >=4):
                generic_error()
                continue
            else:
                print(f"got the option {user_choice}")
        except ValueError:
            generic_error()
            continue
        else:
            return user_choice
            break

