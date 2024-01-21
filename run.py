from master import create_app
from flask import session
from datetime import timedelta

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    session.permanent = True
    app.permanent_session_lifetime = timedelta(days=30)
