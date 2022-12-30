# main file for WorldOfGames

from Live import welcome, load_game
import guess_game, MainScores, e2e, Utils




def start():
    welcome(Utils.USER_NAME)
    [game_selected, game_level] = load_game()
    print(f"OK, let's play game number: {game_selected}")
    print(f"The game level was set to: {game_level}")
    
    if game_selected == 1:
        print("\n=================== Guess Game ===============")
        guess_game.main(game_level)
    else:
        print("\n=================== other Game ===============")
        print("\nGame is not ready yet...")
        exit
        
def check_replay():
    while Utils.REPLAY:
        try:
            user_input = str(input("\nWould you like to play again? [y/n]"))
            if user_input == "y":
                print("\nHere we got again...")
                start()
            else:
                print("Ok, I guess this is the end... bye bye for now. ")
                Utils.REPLAY = False
                exit
                
        except ValueError:
            Utils.generic_error()
            continue
    print("Closing down...")     

def main():
    
    Utils.start_web_server()
    Utils.sleep(3)
    start()
    check_replay()
    last_score = MainScores.get_score()
    Utils.print_effect(f"\nWell done {Utils.USER_NAME} your last_score is {last_score}\n")
    e2e.main()
    

if __name__ == '__main__':
    main()