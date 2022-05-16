#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def path():
    """
    Function that display text on screen - web route (/).
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def path_hbnb():
    """
    Function that display text on screen - web route (/hbnb).
    """
    return 'HBNB'


@app.route('/c/<custom>', strict_slashes=False)
def path_c_custom(custom):
    """
    Function that display custom *text* on screen.
    * Web route custom (/c/<custom>).
    Args:
        custom (str): Custom number (/<custom> -> parameter)
    """
    return 'C %s' % custom.replace('_', ' ')


@app.route('/python', defaults={'custom': 'is cool'}, strict_slashes=False)
@app.route('/python/<path:custom>', strict_slashes=False)
def path_python_custom(custom):
    """
    Function that display custom *text* on screen.
    * Web route custom (/python/<custom>).
    Args:
        custom (str): Custom number (/<path:custom> -> parameter)
    """
    return "Python {}".format(custom.replace('_', ' '))


@app.route('/number/<int:number>', strict_slashes=False)
def path_number_custom(number):
    """
    Function that display custom *int* on screen.
    * Web route custom (/number/<number>).
    Args:
        number (int): Custom number (/<int:number> -> parameter)
    """
    return "{} is a number".format(number)


@app.route('/number_template/<int:number>', strict_slashes=False)
def path_number_template(number):
    """
    Function that display custom *int* on screen.
    * Web route custom (/number_template/<number>).
    Args:
        number (int): Custom number (/<int:number> -> parameter)
    """
    return render_template('5-number.html', number=number)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
