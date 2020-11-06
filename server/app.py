from flask import Flask

from server.router import bp


def create_app():
    _app = Flask(__name__)

    _app.register_blueprint(bp)

    return _app
