#!/usr/bin/python3
"""
This module defines a Flask web application
that displays "Hello HBNB!", "HBNB", and "C <text>".
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
