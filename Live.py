
def welcome(name):
    print (f"Hello {name} and welcome to the World of Games (WoG).\n Here you can find many cool games to play.")

def generic_error():
    print("Not a good selection, please enter a valid option! Try again.")
    return

def input_validation(message, max_value):
    while True:
        try:
            user_input = int(input(f"{message}"))
            if (user_input <= 0) or (user_input >= max_value):
                generic_error()
                continue
            else:
                print(f"User choose option number {user_input}")
        except ValueError:
            generic_error()
            continue
        else:
            return user_input
            break

def load_game():
    game_options = {
        "1": "Memory Game -\n a sequence of numbers will appear for 1 second and you have to guess it back",
        "2": "Guess Game -\n guess a number and see if you chose like the computer",
        "3": "Currency Roulette -\n try and guess the value of a random amount of USD in ILS"
    }

    for k,v in game_options.items():
        print(f"{k}. {v} \n")

    game_message = "Please enter your option: \n"

    max_option = len(game_options.keys()) + 1
    game_option = input_validation(game_message, max_option)

    message_level = """
    Please choose game difficulty from 1 to 5:
    """
    max_difficulty = 6
    game_level = input_validation(message_level, max_difficulty)

    return game_option, game_level
