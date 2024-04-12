#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage, classes
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Displays html with states listed
    """
    states = storage.all(classes["State"]).values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return (render_template('8-cities_by_states.html', states=states_sorted))


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """
    Displays html with states and cities listed
    """
    states = storage.all(classes["State"]).values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return (render_template('8-cities_by_states.html', states=states_sorted))


@app.teardown_appcontext
def teardown_db(exception):
    """
    Close storage session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
