#!/usr/bin/python3
# Import necessary modules from flask and models
from flask import Flask, render_template
from models import storage, State, Amenity

# Create an instance of the Flask class
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Define a route for '/hbnb_filters' with strict_slashes set to False"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    amenities = sorted(storage.all(Amenity).values(),
                       key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """Define a function to be called when cleaning up after a response"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
