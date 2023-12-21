from flask import render_template, Blueprint
from flask import session

medications = Blueprint('medications', __name__)


@medications.route("/medications/calcium")
def calcium():    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']
    ptAdult = False
    ptMax100 = False
    if ptYears >= 18:
        ptAdult = True
        ptMax100 = False
    else:

        if ptKgs >= 100:
            ptAdult = False
            ptMax100 = True
        else:
            ptMax100 = False

    return render_template('/medications/calcium.html', ptAdult=ptAdult, ptMax100=ptMax100, ptYears=ptYears, ptKgs=ptKgs)

@medications.route("/medications/dexamethasone")
def dexamethasone():    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']
    ptAdult = False
    ptMax26 = False
    if ptYears >= 18:
        ptAdult = True
        ptMax26 = False
    else:

        if ptKgs > 26.6:
            ptAdult = False
            ptMax26 = True
        else:
            ptMax26 = False

    return render_template('/medications/dexamethasone.html', ptAdult=ptAdult, ptMax26=ptMax26, ptYears=ptYears, ptKgs=ptKgs)

@medications.route("/medications/diltiazem")
def diltiazem():    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']
    ptAdult = False
    if ptYears >= 18:
        ptAdult = True
    else:
        ptAdult = False

    return render_template('/medications/diltiazem.html', ptAdult=ptAdult, ptYears=ptYears, ptKgs=ptKgs)