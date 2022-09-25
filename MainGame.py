# main file for WorldOfGames

from Live import welcome, load_game, game_level

if __name__ == '__main__':
    welcome("Shay")
    game_selected = load_game()
    print(f"OK, let's play game number: {game_selected}")
    user_lavel = game_level()
    print(f"OK, set the game level to: {user_lavel}")