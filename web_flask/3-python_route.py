#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ display a message """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ display a message """
    return 'HBNB'


@app.route('/c/<text>')
def c_isfun(text):
    """ display “C ” followed by the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def python_(text='is cool'):
    """
    display “Python ”, followed by the value of the text variable,
    with default value of text: "is cool"
    """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
