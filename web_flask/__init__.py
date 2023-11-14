#!/usr/bin/python3
from web_flask import app


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"
