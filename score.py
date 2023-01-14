"""
A package that is in charge of managing the scores file.

The scores file at this point will consist of only a number. 
That number is the accumulation of the winnings of the user. 

Amount of points for winning a game is as follows:
POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
Each time the user is winning a game, the points he one will be added to his current amount of
point saved in a file.

Methods
------------
1. add_score - The function input is a variable called difficulty. The function will try to read
the current score in the scores file, if it fails it will create a new one and will use it to save
the current score.

"""
import os.path
#import Utils

#
# get the last results reported in the score file
# If files still does not exist last_score = 0
#
def get_last_line(source_file):
  with open(source_file, "rb") as file:
    try:
      file.seek(-2, os.SEEK_END)
      while file.read(1) != b'\n':
        file.seek(-2, os.SEEK_CUR)
    except OSError:
      file.seek(0)
      
    last_score = file.readline().decode()
      
  #print(f"this is the last score: {last_score}")
  return int(last_score)



# add new score to the score file
def add_score(difficulty, score_file):
  points_of_winning = (difficulty * 3) + 5
  last_score = get_last_line(score_file)
  new_score = int(last_score) + int(points_of_winning)
  print(f"\nUser got a new score {new_score}!!!")
  
  with open(score_file, 'a') as file:
    file.write("\n" + str(new_score))
  
  print("\nA new score was added to the score file")
  
def main(utils_obj, difficulty):
  file_name=utils_obj.SCORES_FILE_NAME
  #Create scores file if it does not exist
  # add score 0 to the file
  if not os.path.isfile(file_name):
    with open(file_name, 'w') as file:
      file.write("This is the scores file: \n0")  
    
  add_score(difficulty, file_name)
  
  with open(file_name, 'r') as file:
    data = file.read()
  
  print (f"The file {file_name} contain these info: \n{data}")


if __name__ == "__main__":
    main()
    
    

    