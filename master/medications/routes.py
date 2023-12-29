from flask import render_template, Blueprint
from flask import session

medications = Blueprint('medications', __name__)

@medications.route("/medications/acetaminophen")
def acetaminophen():    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']
    ptAdult = False
    ptMax43 = False
    if ptYears >= 18:
        ptAdult = True
        ptMax43 = False
    else:

        if ptKgs >= 43:
            ptAdult = False
            ptMax43 = True
        else:
            ptMax43 = False

    return render_template('/medications/acetaminophen.html', ptAdult=ptAdult, ptMax43=ptMax43, ptYears=ptYears, ptKgs=ptKgs, varTitle="Acetaminophen")

@medications.route("/medications/adenosine")
def adenosine():    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']
    ptAdult = False
    ptMax60 = False
    if ptYears >= 18:
        ptAdult = True
        ptMax60 = False
    else:

        if ptKgs >= 60:
            ptAdult = False
            ptMax60 = True
        else:
            ptMax60 = False

    return render_template('/medications/adenosine.html', ptAdult=ptAdult, ptMax60=ptMax60, ptYears=ptYears, ptKgs=ptKgs, varTitle="Adenosine")

@medications.route("/medications/albuterol")
def albuterol():    
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

    return render_template('/medications/albuterol.html', ptAdult=ptAdult, ptYears=ptYears, ptKgs=ptKgs, varTitle="Albuterol")

@medications.route("/medications/aspirin")
def aspirin():    
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

    return render_template('/medications/aspirin.html', ptAdult=ptAdult, ptYears=ptYears, ptKgs=ptKgs, varTitle="Aspirin")

@medications.route("/medications/atropine")
def atropine():    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']

    ptAdult = False
    ptYrs8 = False
    ptKg5Min = False
    ptMax25 = False
    ptMax50 = False

    if ptYears <= 8:
        ptAdult = False
        ptYrs8 = False

    elif ptYears >= 18:
        ptAdult = True
        ptYrs8 = True
    else:
        ptAdult = False
        ptYrs8 = True


    if ptKgs >= 50:
        ptKg5Min = True
        ptMax25 = True
        ptMax50 = True

    elif ptKgs >= 25:
        ptKg5Min = True
        ptMax25 = True
        ptMax50 = False

    elif ptKgs >= 5:
        ptKg5Min = True
        ptMax25 = False
        ptMax50 = False

    else:
        ptKg5Min = False
        ptMax25 = False
        ptMax50 = False

   

    return render_template('/medications/atropine.html', ptAdult=ptAdult, ptYears=ptYears, ptYrs8=ptYrs8, ptKgs=ptKgs, ptMax50=ptMax50, ptMax25=ptMax25, ptKg5Min=ptKg5Min, varTitle="Atropine")

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

    return render_template('/medications/calcium.html', ptAdult=ptAdult, ptMax100=ptMax100, ptYears=ptYears, ptKgs=ptKgs, varTitle="Calcium")

@medications.route("/medications/cefazolin")
def cefazolin():    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']
    ptAdult = False
    ptKgsMin = False
    ptKgsMax = False

    if ptYears >= 18:
        ptAdult = True
    else:
        ptAdult = False

    if ptKgs >= 120:
        ptKgsMax = True
        ptKgsMin = True
    elif ptKgs >= 40:
        ptKgsMax = False
        ptKgsMin = True
    else:
        ptKgsMax = False
        ptKgsMin = False

    return render_template('/medications/cefazolin.html', ptAdult=ptAdult, ptKgsMax=ptKgsMax, ptKgsMin=ptKgsMin, ptYears=ptYears, ptKgs=ptKgs, varTitle="Cefazolin")

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

    return render_template('/medications/dexamethasone.html', ptAdult=ptAdult, ptMax26=ptMax26, ptYears=ptYears, ptKgs=ptKgs, varTitle="Dexamethasone")

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

    return render_template('/medications/diltiazem.html', ptAdult=ptAdult, ptYears=ptYears, ptKgs=ptKgs, varTitle="Diltiazem")

@medications.route("/medications/diphenhydramine")
def diphenhydramine():    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']
    ptAdult = False
    ptMax50 = False

    if ptYears >= 18:
        ptAdult = True
    else:
        ptAdult = False

    if ptKgs >= 50:
        ptMax50 = True
    else:
        ptMax50 = False

    return render_template('/medications/diphenhydramine.html', ptAdult=ptAdult, ptMax50=ptMax50, ptYears=ptYears, ptKgs=ptKgs, varTitle="Diphenhydramine")

@medications.route("/medications/dopamine")
def dopamine():    

    return render_template('/medications/dopamine.html', varTitle="Dopamine")

@medications.route("/medications/droperidol")
def droperidol():    
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

    return render_template('/medications/droperidol.html', ptAdult=ptAdult, ptYears=ptYears, ptKgs=ptKgs, varTitle="Droperidol")

