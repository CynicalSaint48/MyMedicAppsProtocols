import json


class Config:
    SECRET_KEY = '479b64a67109351b2b5b21c6e2ec17ad'
    SQLALCHEMY_DATABASE_URI = 'site.db'
    MAIL_SERVER = 'smtp.1and1.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'Eusername'
    MAIL_PASSWORD = 'Epassword'
