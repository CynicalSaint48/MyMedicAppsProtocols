from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from master.config import Config
from flask_mail import Mail
from datetime import datetime





bcrypt = Bcrypt()

db = SQLAlchemy()
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

# app = create_app()

# app = Flask(__name__)
# db = SQLAlchemy(app)
# bob = 'ur uncle'

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120),  unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)



#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
# class UpdatePost(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     date_protocol = db.Column(db.String(10), nullable=False)
#     description = db.Column(db.Text, nullable=False)
