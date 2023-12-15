from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from master.config import Config




db = SQLAlchemy()
bcrypt = Bcrypt()
SECRET_KEY = 'thisisnotasecret'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    print(SECRET_KEY)

    from master.protocols.routes import protocols
    from master.main.routes import main
    app.register_blueprint(protocols)
    app.register_blueprint(main)

    return app