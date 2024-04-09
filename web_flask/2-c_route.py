#!/usr/bin/python3
'''
    Script that starts a Flask web application
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''
        Returns a string to the root route / of the web application
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
        Returns a string to the route /hbnb of the web application
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    '''
        Returns a string to the route /c/<text> of the web application,
        that exchanges text for the value of the text variable
    '''
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
