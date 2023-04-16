from flask import Flask, render_template
import random
from datetime import date
import requests
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 100)
    current_year = (datetime.datetime.now().year)
    return render_template("index2.html", num=random_number, year=current_year)









if __name__ == "__main__":
    app.run()