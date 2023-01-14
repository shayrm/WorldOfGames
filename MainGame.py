# main file for WorldOfGames

from Live import welcome, load_game
import guess_game, MainScores, e2e, Utils


def start(utils_obj):
    welcome(utils_obj)
    [game_selected, game_level] = load_game(utils_obj)
    print(f"OK, let's play game number: {game_selected}")
    print(f"The game level was set to: {game_level}")
    
    if game_selected == 1:
        print("\n=================== Guess Game ===============")
        guess_game.main(utils_obj, game_level)
    else:
        print("\n=================== other Game ===============")
        print("\nGame is not ready yet...")
        exit
        
def check_replay(utils_obj):
    while utils_obj.REPLAY:
        try:
            user_input = str(input("\nWould you like to play again? [y/n]"))
            if user_input == "y":
                print("\nHere we got again...")
                utils_obj.first_round = False
                start(utils_obj)
            else:
                print("Ok, I guess this is the end... bye bye for now. ")
                utils_obj.REPLAY = False
                exit
                
        except ValueError:
            utils_obj.generic_error()
            continue
    print("Closing down...")     

def main():
    utils_obj = Utils.main()
    utils_obj.start_web_server()
    utils_obj.time_out(3)
    start(utils_obj)
    check_replay(utils_obj)
    last_score = MainScores.get_score(utils_obj)
    utils_obj.print_effect(f"\nWell done {utils_obj.USER_NAME} your last_score is {last_score}\n")
    if utils_obj.PLATFORM == "loacl":
        e2e.main()
    else:
        print(f"{utils_obj.USER_NAME}, it was pleasure to play with you... see you next time.")

if __name__ == '__main__':
    main()