#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!'
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB'
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays C followed by the of text variable
    """
    return 'C' + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text):
    return 'Python' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
