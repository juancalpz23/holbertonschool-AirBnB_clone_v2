#!/usr/bin/python3
from flask import Flask, render_template
"""
intializing flask web app to listen on 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage, classes


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    """
    Displays 'HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays C followed by the of text variable
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text):
    """
    Display 'Python' followed by text
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_num(n):
    """
    Displays 'n' number only if integer
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_num_template(n):
    """
    Display an HTML page if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_odd_even(n):
    """
    Display a HTML page only if n is an integer, and if it is odd or eve
    """
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Displays html with states listed
    """
    states = storage.all(classes["State"]).values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return (render_template('7-states_list.html', states=states_sorted))


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """
    Displays html with states and cities listed
    """
    states = storage.all(classes["State"]).values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return (render_template('8-cities_by_states.html', states=states_sorted))


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_cities(id=None):
    """
    Displays cities of a specific state or a state
    """
    states = storage.all(classes["State"]).values()
    if id:
        for state in states:
            if state.id == id:
                return render_template('9-states.html', state=state)
        return render_template('9-states.html')
    else:
        return render_template('9-states.html', states=states)


@app.route('/hbnb_filters')
def filters():
    """
    display HBNB HTML page
    """
    states = storage.all(classes["State"]).values()
    amenities = storage.all(classes["Amenity"]).values()
    return (render_template('10-hbnb_filters.html', states=states,
                            amenities=amenities))


@app.teardown_appcontext
def teardown_db(exception):
    """
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
