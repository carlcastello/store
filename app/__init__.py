from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

DATABASE = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    DATABASE.init_app(app)

    from .infrastructure.root import ROOT_BP
    app.register_blueprint(ROOT_BP)

    return app