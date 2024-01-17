from flask import Blueprint, render_template, session
from master.protocols.routes import get_key_list
from decimal import *
from werkzeug.exceptions import HTTPException

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def page_not_found(e):
    keys = get_key_list()
    return render_template('errors/404.html', keys=keys, trace=e), 404

@errors.app_errorhandler(403)
def permission_denied(e):
    keys = get_key_list()
    return render_template('errors/403.html', keys=keys, trace=e), 403

@errors.app_errorhandler(500)
def internal_server_error(e):
    keys = get_key_list()
    return render_template('errors/500.html', keys=keys, trace=e), 500

@errors.app_errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors. You wouldn't want to handle these generically.
    if isinstance(e, HTTPException):
        return e

    keys = get_key_list()
    # now you're handling non-HTTP exceptions only
    return render_template("errors/500.html", trace=e, keys=keys), 500

