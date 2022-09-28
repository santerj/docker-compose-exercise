import os

import requests

from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def hello_world():

    # get values from request object
    remoteAddr = request.environ.get('REMOTE_ADDR')
    remotePort = request.environ.get('REMOTE_PORT')
    serverAddr = request.environ.get('SERVER_NAME')
    serverPort = request.environ.get('SERVER_PORT')

    # make request to Service 2
    r = requests.get(f"http://{os.environ.get('SERVICE2')}")

    return (
        f"Hello from {remoteAddr}:{remotePort}\n"
        f"to {serverAddr}:{serverPort}\n"
        f"{r.text}"
    )


if __name__ == "__main__":
    app.run("0.0.0.0", port=80)