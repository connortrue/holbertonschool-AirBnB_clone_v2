#!/usr/bin/python3
# Import necessary modules from flask and models
from flask import Flask, render_template
from models import storage, State

# Create an instance of the Flask class
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Define a route for '/states' with strict_slashes set to False"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    # Render the 'states.html' template with 'states' as a context variable
    return render_template('states.html', states=states)


# Define a route for '/states/<id>' with strict_slashes set to False
@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Retrieve a State object with the given id"""
    state = storage.get(State, id)
    # If the state exists
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('state.html', state=state, cities=cities)
    # If the state does not exist
    else:
        return render_template('404.html'), 404


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage"""
    storage.close()


# Check if the script is run directly (not imported)
if __name__ == "__main__":
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
