from flask import Flask, render_template, url_for, Blueprint

protocols = Blueprint('protocols', __name__)

# @protocols.route("/")
# @protocols.route("/home")
# def home():
#     return render_template('/protocols/protocol_base.html')

@protocols.route("/protocols/allergic_reaction")
def allergy():
    print('Running protocols.allergy')
    return render_template('/protocols/AllergicReaction.html')