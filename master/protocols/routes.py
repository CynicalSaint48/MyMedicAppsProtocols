from flask import Flask, render_template, url_for, Blueprint
from flask_login import login_user, current_user

protocols = Blueprint('protocols', __name__)

# @protocols.route("/")
# @protocols.route("/home")
# def home():
#     return render_template('/protocols/protocol_base.html')

@protocols.route("/protocols/allergic_reaction")
def allergy():
    return render_template('/protocols/AllergicReaction.html')