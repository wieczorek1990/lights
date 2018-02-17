import flask
import json


app = flask.Flask(__name__)
lights_state = 'off'


@app.route("/")
def lights():
    if lights_state == 'off':
        return "Lights are off."
    elif lights_state == 'on':
        return "Lights are on."
    else:
        flask.abort(500)


@app.route("/control", methods=["POST"])
def control():
    global lights_state
    if not flask.request.json:
        flask.abort(400)
    if 'lights' not in flask.request.json:
        flask.abort(400)
    state = flask.request.json['lights']
    if state not in ('off', 'on'):
        flask.abort(400)
    lights_state = state
    return json.dumps(flask.request.json)

