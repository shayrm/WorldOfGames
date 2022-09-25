

def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\n Here you can find many cool games to play."


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


load_game()