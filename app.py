from flask import Flask, request, jsonify
from services.robo import robo

app = Flask(__name__)


@app.route("/", methods=["POST"])
def command_robo():
    body = request.get_json()

    response = {}

    if not body:
        response["ERROR"] = "no command found, please send a command."

    elif str(body).isdigit():
        response["ERROR"] = "commands can't be numeric."

    else:
        response["position"] = robo(body["commands"])

    return jsonify(response)
