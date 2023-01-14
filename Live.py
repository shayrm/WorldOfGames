"""
Starting point for game options

"""

import Utils

def welcome(utils_obj):
    utils_obj.screen_cleaner()
    message = f"\nHello {utils_obj.USER_NAME} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."
    utils_obj.print_effect(message)
    print("\n-----------------------------------------------------------\n")

def input_validation(utils_obj, message, max_value):
    
    while True:
        try:
            user_input = int(input(f"{message}"))
            if (user_input <= 0) or (user_input >= max_value):
                utils_obj.generic_error()
                continue
            else:
                print(f"User choose option number {user_input}")
        except ValueError:
            utils_obj.generic_error()
            continue
        else:
            return user_input
            break

def load_game(utils_obj):
    #load the list of game options from the utils object as a dictionaly 
    game_options = utils_obj.game_options()
    
    game_index = 1
    for k,v in game_options.items():
        if game_index < len(k):
            output = f"{game_index}. {k} - {v}"
            utils_obj.print_effect(output)
            game_index += 1

    game_message = "\nPlease enter your option: \n"

    max_option = len(game_options.keys()) + 1
    game_option = input_validation(utils_obj, game_message, max_option)

    message_level = "\nPlease choose game difficulty from 1 to 5:"
    max_difficulty = 6
    game_level = input_validation(utils_obj, message_level, max_difficulty)

    return game_option, game_level
