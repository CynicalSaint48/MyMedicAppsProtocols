from datetime import datetime
from master import db, login_manager
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120),  unique=True, nullable=False)
    displayName = db.Column(db.String(120))
    password = db.Column(db.String(60), nullable=False)
    showNarrative = db.Column(db.Boolean, default=1)
    showBasic = db.Column(db.Boolean, default=1)
    showAdvanced = db.Column(db.Boolean, default=1)
    showAdditional = db.Column(db.Boolean, default=1)

    def get_reset_token(self, expires_sec=1800):
            s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
            return s.dumps({'user_id': self.id}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User(''{self.user_id}', {self.email}')"
    
class UpdatePost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_protocol = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Update(''{self.title}', {self.date_posted}, {self.date_protocol}, {self.description}')"

