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


    return render_template('/protocols/AllergicReaction.html', ptAdult=ptAdult, ptMax26=ptMax26, ptMax30=ptMax30, ptMax50=ptMax50, ptYears=ptYears, ptKgs=ptKgs, varTitle="Allergic Reaction")

@protocols.route("/protocols/abdominal_pain")
def abdominal():

    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']

    ptAdult = False
    ptMax26 = False
    ptMax100 = False


    if ptYears >= 18:
        ptAdult = True
    else:
        ptAdult = False

    if ptKgs >= 100:
            ptMax26 = True
            ptMax100 = True
    elif ptKgs >= 26:
            ptMax26 = True
            ptMax100 = False
    else:
            ptMax26 = False
            ptMax100 = False

    return render_template('/protocols/AbdPain.html', ptAdult=ptAdult, ptMax26=ptMax26, ptMax100=ptMax100, ptYears=ptYears, ptKgs=ptKgs, varTitle="Abdominal Pain")

@protocols.route("/protocols/bites_envenomations")
def bites():

    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']

    ptAdult = False
    ptMax43 = False
    ptMax50 = False
    ptMax100 = False


    if ptYears >= 18:
        ptAdult = True
    else:
        ptAdult = False

    if ptKgs >= 100:
            ptMax43 = True
            ptMax50 = True
            ptMax100 = True

    elif ptKgs >= 50:
            ptMax43 = True
            ptMax50 = True
            ptMax100 = False

    elif ptKgs >= 43:
        ptMax43 = True
        ptMax50 = False
        ptMax100 = False

    else:
            ptMax43 = False
            ptMax50 = False
            ptMax100 = False

    return render_template('/protocols/Bites_Envenomations.html', ptAdult=ptAdult, ptMax43=ptMax43, ptMax50=ptMax50, ptMax100=ptMax100, ptYears=ptYears, ptKgs=ptKgs, varTitle="Bites & Envenomations")

@protocols.route("/protocols/animal_bites")
def animalBites():

    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']

    ptAdult = False
    ptMax43 = False
    ptMax100 = False


    if ptYears >= 18:
        ptAdult = True
    else:
        ptAdult = False

    if ptKgs >= 100:
            ptMax43 = True
            ptMax100 = True

    elif ptKgs >= 43:
        ptMax43 = True
        ptMax100 = False

    else:
            ptMax43 = False
            ptMax100 = False

    return render_template('/protocols/AnimalBites.html', ptAdult=ptAdult, ptMax43=ptMax43, ptMax100=ptMax100, ptYears=ptYears, ptKgs=ptKgs, varTitle="Animal Bites")

@protocols.route("/protocols/assault")
def assault():

    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']

    ptAdult = False
    ptMax40 = False
    ptMax43 = False
    ptMax100 = False
    ptMax120 = False

    if ptYears >= 18:
        ptAdult = True
    else:
        ptAdult = False

    if ptKgs >= 120:
        ptMax40 = True
        ptMax43 = True
        ptMax100 = True
        ptMax120 = True

    elif ptKgs >= 100:
        ptMax40 = True
        ptMax43 = True
        ptMax100 = True
        ptMax120 = False

    elif ptKgs >= 43:
        ptMax40 = True
        ptMax43 = True
        ptMax100 = False
        ptMax120 = False

    elif ptKgs >= 40:
        ptMax40 = True
        ptMax43 = False
        ptMax100 = False
        ptMax120 = False

    else:
        ptMax40 = False
        ptMax43 = False
        ptMax100 = False
        ptMax120 = False

    return render_template('/protocols/Assault.html', ptAdult=ptAdult, ptMax40=ptMax40, ptMax43=ptMax43, ptMax100=ptMax100, ptMax120=ptMax120, ptYears=ptYears, ptKgs=ptKgs, varTitle="Assault")

@protocols.route("/protocols/BackPain")
def backPain():

    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']

    ptAdult = False
    ptMax40 = False
    ptMax43 = False
    ptMax100 = False
    ptMax120 = False

    if ptYears >= 18:
        ptAdult = True
    else:
        ptAdult = False

    if ptKgs >= 120:        
        ptMax26 = True
        ptMax40 = True
        ptMax43 = True
        ptMax100 = True
        ptMax120 = True

    elif ptKgs >= 100:        
        ptMax26 = True
        ptMax40 = True
        ptMax43 = True
        ptMax100 = True
        ptMax120 = False

    elif ptKgs >= 43:        
        ptMax26 = True
        ptMax40 = True
        ptMax43 = True
        ptMax100 = False
        ptMax120 = False

    elif ptKgs >= 40:        
        ptMax26 = True
        ptMax40 = True
        ptMax43 = False
        ptMax100 = False
        ptMax120 = False

    elif ptKgs >= 26:        
        ptMax26 = True
        ptMax40 = False
        ptMax43 = False
        ptMax100 = False
        ptMax120 = False


    else:        
        ptMax26 = False
        ptMax40 = False
        ptMax43 = False
        ptMax100 = False
        ptMax120 = False

    return render_template('/protocols/BackPain.html', ptAdult=ptAdult, ptMax26=ptMax26, ptMax40=ptMax40, ptMax43=ptMax43, ptMax100=ptMax100, ptMax120=ptMax120, ptYears=ptYears, ptKgs=ptKgs, varTitle="Back Pain")

@protocols.route("/protocols/BreathingProblems")
def breathingProblems():

    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']

    ptAdult = False

    ptMax20 = False
    ptMax26 = False
    ptMax30 = False
    ptMax33 = False
    ptMax40 = False
    ptMax100 = False

    if ptYears >= 18:
        ptAdult = True
    else:
        ptAdult = False

    if ptKgs >= 100:        
        ptMax20 = True
        ptMax26 = True
        ptMax30 = True
        ptMax33 = True
        ptMax40 = True
        ptMax100 = True

    elif ptKgs >= 40:        
        ptMax20 = True
        ptMax26 = True
        ptMax30 = True
        ptMax33 = True
        ptMax40 = True
        ptMax100 = False

    elif ptKgs >= 33:        
        ptMax20 = True
        ptMax26 = True
        ptMax30 = True
        ptMax33 = True
        ptMax40 = False
        ptMax100 = False

    elif ptKgs >= 30:        
        ptMax20 = True
        ptMax26 = True
        ptMax30 = True
        ptMax33 = False
        ptMax40 = False
        ptMax100 = False

    elif ptKgs >= 26:        
        ptMax20 = True
        ptMax26 = True
        ptMax30 = False
        ptMax33 = False
        ptMax40 = False
        ptMax100 = False

    elif ptKgs >= 20:        
        ptMax20 = True
        ptMax26 = False
        ptMax30 = False
        ptMax33 = False
        ptMax40 = False
        ptMax100 = False


    else:        
        ptMax20 = False
        ptMax26 = False
        ptMax30 = False
        ptMax33 = False
        ptMax40 = False
        ptMax100 = False

    return render_template('/protocols/BreathingProblems.html', ptAdult=ptAdult, ptMax20=ptMax20, ptMax26=ptMax26, ptMax30=ptMax30, ptMax33=ptMax33, ptMax40=ptMax40, ptMax100=ptMax100, ptYears=ptYears, ptKgs=ptKgs, varTitle="Breathing Problems")

@protocols.route("/protocols/Burns")
def burns():

    
    if not session['ptYears']:
        ptYears = 0
        ptKgs = 0.0
    else:
        ptYears = session['ptYears']
        ptKgs = session['ptKgs']

    ptAdult = False

    ptMax43 = False
    ptMax50 = False
    ptMax100 = False

    if ptYears >= 18:
        ptAdult = True
    else:
        ptAdult = False

    if ptKgs >= 100:        
        ptMax43 = True
        ptMax50 = True
        ptMax100 = True

    elif ptKgs >= 50:        
        ptMax43 = True
        ptMax50 = True
        ptMax100 = False

    elif ptKgs >= 43:    
        ptMax43 = True
        ptMax50 = False
        ptMax100 = False

    else:
        ptMax43 = False
        ptMax50 = False
        ptMax100 = False

    return render_template('/protocols/Burns.html', ptAdult=ptAdult, ptMax43=ptMax43, ptMax50=ptMax50, ptMax100=ptMax100, ptYears=ptYears, ptKgs=ptKgs, varTitle="Burns")