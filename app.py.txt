# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

names = []

@app.route('/')
def index():
    return render_template('index.html', names=names)

@app.route('/save', methods=['POST'])
def save_name():
    name = request.form['name']
    names.append(name)
    return render_template('index.html', names=names)

if __name__ == '__main__':
    app.run()
