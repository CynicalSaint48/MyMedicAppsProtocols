from master import create_app
from flask import session, request, has_request_context
from datetime import timedelta
import logging
from logging.handlers import RotatingFileHandler

app = create_app()

logger = logging.getLogger()
class NewFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote = request.remote_addr
        else:
            record.url = None
            record.remote = None
        return super().format(record)

logFormatter = NewFormatter("%(asctime)s - %(url)s - %(remote)s - %(levelname)s - %(message)s", datefmt="%m-%d-%Y %H:%M:%S")


# Add console Handler to the root logger
consoleHandler = logging.StreamHandler()
logger.addHandler(consoleHandler)

# Add File Handler to the root logger
fileHandler = RotatingFileHandler('errors.log', maxBytes=1024, backupCount=5)
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(days=30)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
    
