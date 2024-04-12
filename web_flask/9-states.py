#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage, classes
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """
    Displays a list of states
    """
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return render_template('states.html', states=states_sorted)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """
    Displays cities of a specific state
    """
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('state.html', state=state, cities=cities)
    else:
        return render_template('not_found.html')


@app.teardown_appcontext
def teardown_db(exception):
    """
    Close session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
