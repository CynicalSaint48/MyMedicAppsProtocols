# tools/routes.py

from flask import render_template, Blueprint
from flask import session, request
from master.protocols.routes import get_key_list


tools = Blueprint('tools', __name__)

@tools.route("/tools/PhoneNumbers")
def phoneNumbers():

    keys = get_key_list()
    session['path'] = 'main.home'
    return render_template('/tools/PhoneNumbers.html', keys=keys, varTitle="Useful Phone Numbers")

