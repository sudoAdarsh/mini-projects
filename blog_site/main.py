from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.now().year
    return render_template("index.html", year=current_year)

@app.route('/guess/<username>')
def guess(username):
    response = requests.get(f"https://api.agify.io?name={username}")
    age = response.json()["age"]

    response = requests.get(f"https://api.genderize.io?name={username}")
    gender = response.json()["gender"]

    return render_template("guess.html", name=username.capitalize(), age=age, gender=gender)
if __name__ == "__main__":
    app.run(debug=True)