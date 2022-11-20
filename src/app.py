import flask
from flask import Flask, Blueprint
from flask_cors import CORS
from config import set_app_configs


def get_app():
    from api.routes import urls_blueprint

    app = Flask(__name__)
    CORS(app)
    set_app_configs(app)
    app.register_blueprint(urls_blueprint)
    return app
