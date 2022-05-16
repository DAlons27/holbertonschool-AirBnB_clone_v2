#!/usr/bin/python3
""" Script that starts a Flask weeb application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.route('/hbnb/', strict_slashes=False)
def path_states_list():
    """ Function display en teemplated state and amenities list
    in 6-index.html (web_static)"""
    all_states = storage.all(State).values()
    all_amenities = storage.all(Amenity).values()
    all_places = storage.all(Place).values()

    return render_template(
        '100-hbnb.html',
        states=all_states,
        amenities=all_amenities,
        places=all_places
    )


@app.teardown_appcontext
def teardown_close_session(exception):
    """ Function to be calledd when the application context ends. """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
