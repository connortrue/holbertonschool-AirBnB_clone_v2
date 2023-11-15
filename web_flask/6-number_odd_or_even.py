#!/usr/bin/python3
"""
This module defines a Flask web application
that displays "Hello HBNB!", "HBNB", "C <text>", "Python <text>",
"<n> is a number", a HTML page with "Number: <n>", and a HTML page
with "Number: <n> is even|odd".
"""
from flask import Flask, render_template
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
    """Displays 'Python <text>', with underscores in <text>
    replaced by spaces."""
    text = text.replace('_', ' ')
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """Displays '<n> is a number' if n is an integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays a HTML page with 'Number: <n>' if n is an integer."""
    return render_template('number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays a HTML page with 'Number: <n> is even|odd' if
    n is an integer."""
    return render_template('number_odd_or_even.html',
                           n=n, parity='even' if n % 2 == 0 else 'odd')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
