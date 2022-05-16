#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', defaults={'id': None}, strict_slashes=False)
@app.route('/states/<path:id>', strict_slashes=False)
def path_states_list(id):
    """ Function display en templated state list """
    all_states = storage.all(State)

    if not id:
        return render_template(
            '7-states_list.html',
            items=all_states.values()
        )

    _state = "State.{}".format(id)
    if _state in all_states:
        return render_template(
            '9-states.html',
            state="State: {}".format(all_states[_state].name),
            items=all_states[_state])

    return render_template('9-states.html', items=None)


@app.teardown_appcontext
def teardown_close_session(exception):
    """ Function to be called when the application context ends. """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
