import json


class Config:
    SECRET_KEY = 'thisisnotasecret'
    SQLALCHEMY_DATABASE_URI = 'site.db'
    MAIL_SERVER = 'smtp.1and1.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'Eusername'
    MAIL_PASSWORD = 'Epassword'
