from flask import Flask
from random import randint
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

num = randint(0,9)

@app.route("/<guess>")
def guess(guess):
    if num == int(guess):
        return "<h1 style='color:green;''>You found me!</h>" \
        "<br>" \
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif', width=700>"
    elif num > int(guess):
        return "<h1 style='color:red;''>Too low, try again!</h>" \
        "<br>" \
        "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif', width=700>"
    elif num < int(guess): 
        return "<h1 style='color:purple;''>Too high, try again!</h>" \
        "<br>" \
        "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif', width=700>"
    
if __name__ == "__main__":
    app.run(debug=True)