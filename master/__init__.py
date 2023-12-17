from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from master.config import Config
from flask_mail import Mail
from sqlalchemy import Column, Boolean, DateTime, Integer

from flask_login import login_user, current_user



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager=LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'danger'

mail = Mail()
position = ""


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from master.protocols.routes import protocols
    from master.main.routes import main
    from master.users.routes import users

    from master import models

    app.register_blueprint(protocols)
    app.register_blueprint(main)
    app.register_blueprint(users)

    return app