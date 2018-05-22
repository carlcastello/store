from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config


DATABASE = SQLAlchemy()

def create_app(config_name):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config[config_name])
    config[config_name].init_app(flask_app)

    DATABASE.init_app(flask_app)

    from .infrastructure.routes import ROUTES_BP
    flask_app.register_blueprint(ROUTES_BP)

    return flask_app