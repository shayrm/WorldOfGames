# main file for WorldOfGames

from Live import welcome, load_game
import guess_game

if __name__ == '__main__':

    welcome("Shay")
    [game_selected, game_level] = load_game()
    print(f"OK, let's play game number: {game_selected}")
    print(f"The game level was set to: {game_level}")
    
    if game_selected == 1:
        print("=================== Guess Game ===============")
        guess_game.main(game_level)
    else:
        print("=================== other Game ===============")
        print("Game is not ready yet...")
        exit
        
