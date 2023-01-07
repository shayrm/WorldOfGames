"""
Starting point for game options

"""

import Utils

def welcome(name):
    Utils.screen_cleaner()
    message = f"\nHello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."
    Utils.print_effect(message)
    print("\n-----------------------------------------------------------\n")

def input_validation(message, max_value):
    while True:
        try:
            user_input = int(input(f"{message}"))
            if (user_input <= 0) or (user_input >= max_value):
                Utils.generic_error()
                continue
            else:
                print(f"User choose option number {user_input}")
        except ValueError:
            Utils.generic_error()
            continue
        else:
            return user_input
            break

def load_game():
    game_options = {
        "Guess Game": "Guess a number and see if you chose like the computer\n",
        "Memory Game": "a sequence of numbers will appear for 1 second and you have to guess it back\n",
        "Currency Roulette": "Try and guess the value of a random amount of USD in ILS\n"
    }
    
    game_index = 1
    for k,v in game_options.items():
        if game_index < len(k):
            output = f"{game_index}. {k} - {v}"
            Utils.print_effect(output)
            game_index += 1

    game_message = "\nPlease enter your option: \n"

    max_option = len(game_options.keys()) + 1
    game_option = input_validation(game_message, max_option)

    message_level = "\nPlease choose game difficulty from 1 to 5:"
    max_difficulty = 6
    game_level = input_validation(message_level, max_difficulty)

    return game_option, game_level
