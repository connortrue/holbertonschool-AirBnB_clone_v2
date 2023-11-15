#!/usr/bin/python3
"""
This module defines a Flask web application
that displays "Hello HBNB!", "HBNB", "C <text>", and "Python <text>".
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays 'C <text>', with underscores in <text> replaced by spaces."""
    text = text.replace('_', ' ')
    return "C " + text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Displays 'Python <text>', with underscores in
    <text> replaced by spaces."""
    text = text.replace('_', ' ')
    return "Python " + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
