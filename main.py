from flask import Flask, render_template
import csv
import random

app = Flask(__name__)

with open('col3.csv') as csvfile:
    data = list(csv.reader(csvfile))

@app.route('/')
def index():
    # Get random entry from data
    item = random.choice(data)
    return render_template("index.html", year=item[5], link=item[6])

app.run(host='0.0.0.0', port=81)