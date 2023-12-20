from flask import render_template, Blueprint
from flask import session

protocols = Blueprint('protocols', __name__)

@protocols.route("/protocols/allergic_reaction")
def allergy():

    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']

    ptAdult = False
    ptMax26 = False
    ptMax30 = False
    ptMax50 = False


    if ptYears >= 18:
        ptAdult = True
        ptMax26 = False
        ptMax30 = False
        ptMax50 = False
    else:

        if ptKgs > 26.6:
            ptAdult = False
            ptMax26 = True
            ptMax30 = False
            ptMax50 = False
        if ptKgs >= 30:
            ptAdult = False
            ptMax26 = True
            ptMax30 = True
            ptMax50 = False
        if ptKgs >= 50:
            ptAdult = False
            ptMax26 = True
            ptMax30 = True
            ptMax50 = True
        else:
            ptMax16 = False
            ptMax30 = False
            ptMax50 = False


    return render_template('/protocols/AllergicReaction.html', ptAdult=ptAdult, ptMax26=ptMax26, ptMax30=ptMax30, ptMax50=ptMax50, ptYears=ptYears, ptKgs=ptKgs)