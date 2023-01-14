
import random
import score

class Guess_Game:
  """
  The purpose of guess game is to start a new game, cast a random number between 1 to a
  variable called difficulty . The game will get a number input from the Properties:
  
  1. Difficulty
  2. Secret number
  
  Methods
  1. generate_number - Will generate number between 1 to difficulty and save it to
  secret_number.
  2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and
  return the number.
  3. compare_results - Will compare the the secret generated number to the one prompted
  by the get_guess_from_user.
  4. play - Will call the functions above and play the game. Will return True / False if the user
  lost or won.
  """
    
  def __init__(self, utils_obj, difficulty) -> None:
    self.difficulty = int(difficulty)
    self.utils_obj = utils_obj
    self.match = False
    
  def generate_number(self):  
    self.secret_number = random.randrange(1, self.difficulty + 1) 
    print(f"Generate a secret number equals to: {self.secret_number}")
  
  def get_guess_from_user(self):  
    # generate number between 1 to difficulty and save it to secret_number.        
    self.user_guess = int(input("PLease enter your guessed number: "))
    print(f"Got the number {self.user_guess} from the user")
  
  def compare_results(self):
    print(f"Comparing secret number {self.secret_number} with user input {self.user_guess}")
    if self.secret_number == self.user_guess:
      self.match = True
      
  def play(self):  
    self.generate_number()
    self.get_guess_from_user()
    self.compare_results()
    
    if self.match == True:
      print("\n========================================")
      print(f"We got a winner!!!\n Our secret number {self.secret_number} is equal to your guessed number {self.user_guess}")
      print("========================================\n")
      score.main(self.utils_obj, self.difficulty)
    else:
      print("Nop, you missed it. This is not the chosen number")
            
def main(utils_obj, difficulty):
  game1 = Guess_Game(utils_obj, difficulty)
  game1.play()  

if __name__ == "__main__":
  main()
