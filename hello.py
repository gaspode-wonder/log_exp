# app.py (Flask application)
from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    data = []
    with open('sensor_data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)