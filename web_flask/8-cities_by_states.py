#!/usr/bin/python3
"""
This module defines a Flask web application
that displays a HTML page with the list of all State objects present
in DBStorage sorted by name, and the list of City objects linked to each
State sorted by name.
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays a HTML page with the list of all State objects present in
    DBStorage sorted by name, and the list of City objects linked to each
    State sorted by name."""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy Session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
