"""
# MainScores.py

This file purpose is to serve the user’s score currently in the scores.txt file over HTTP with
HTML. This will be done by using python’s flask library.

Methods
1. score_server - This function will serve the score. It will read the score from the scores file
and will return an HTML that will be as follows:

For that I used the `render_template` method with two html files that stores in `templates` directory.

<html>
  <head>
    <title>Scores Game</title>
  </head>
  <body>
    <h1>The score is <div id="score">{SCORE}</div></h1>
  </body>
</html>

If the function will have a problem showing the result of reading the error it will return the
following:

<html>
  <head>
    <title>Scores Game</title>
  </head>
  <body>
    <h1><div id="score" style="color:red">{ERROR}</div></h1>
  </body>
</html>

"""

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

from flask import Flask, render_template
import score, Utils


app = Flask(__name__)

def get_name():
  name = Utils.USER_NAME
  return name

def get_score():
  file_name = Utils.SCORES_FILE_NAME
  last_score = score.get_last_line(file_name)
  return last_score 

@app.route("/")
def home():
  name = get_name()
  score = get_score()
  return render_template('home_page.html', name = name, score = score)

#@app.route("/<name>")
#def user_path(name):
#  output_page = f"<h1> Hello dear {name}! Hope all is good.</h1>"
#  return output_page

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error = "No Score and no Page"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html', error = "No score and Internal Server Error"), 500

def main():
  app.run()

if __name__ == "__main__":
  main()
  
