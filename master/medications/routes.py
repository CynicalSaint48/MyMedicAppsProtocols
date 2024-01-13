from flask import render_template, Blueprint
from flask import session
from decimal import *
from master.protocols.routes import get_key_list

medications = Blueprint('medications', __name__)

@medications.route("/medications/acetaminophen")
def acetaminophen():    
    
    keys = get_key_list()
    session['path'] = 'medications.acetaminophen'
    return render_template('/medications/acetaminophen.html', keys=keys, varTitle="Acetaminophen")

@medications.route("/medications/adenosine")
def adenosine():    
    
    keys = get_key_list()
    session['path'] = 'medications.adenosine'
    return render_template('/medications/adenosine.html', keys=keys, varTitle="Adenosine")

@medications.route("/medications/albuterol")
def albuterol():    
    
    keys = get_key_list()
    session['path'] = 'medications.albuterol'
    return render_template('/medications/albuterol.html', keys=keys, varTitle="Albuterol")

@medications.route("/medications/aspirin")
def aspirin():    
    
    keys = get_key_list()
    session['path'] = 'medications.aspirin'
    return render_template('/medications/aspirin.html', keys=keys, varTitle="Aspirin")

@medications.route("/medications/atropine")
def atropine():    
    
    keys = get_key_list()
    session['path'] = 'medications.atropine'
    return render_template('/medications/atropine.html', keys=keys, varTitle="Atropine")

@medications.route("/medications/calcium")
def calcium():    
    
    keys = get_key_list()
    session['path'] = 'medications.calcium'
    return render_template('/medications/calcium.html', keys=keys, varTitle="Calcium")

@medications.route("/medications/cefazolin")
def cefazolin():    
    
    keys = get_key_list()
    session['path'] = 'medications.cefazolin'
    return render_template('/medications/cefazolin.html', keys=keys, varTitle="Cefazolin")

@medications.route("/medications/dexamethasone")
def dexamethasone():    
    
    keys = get_key_list()
    session['path'] = 'medications.dexamethasone'
    return render_template('/medications/dexamethasone.html', keys=keys, varTitle="Dexamethasone")

@medications.route("/medications/diltiazem")
def diltiazem():    
    
    keys = get_key_list()
    session['path'] = 'medications.diltiazem'
    return render_template('/medications/diltiazem.html', keys=keys, varTitle="Diltiazem")

@medications.route("/medications/diphenhydramine")
def diphenhydramine():    
    
    keys = get_key_list()
    session['path'] = 'medications.diphenhydramine'
    return render_template('/medications/diphenhydramine.html', keys=keys, varTitle="Diphenhydramine")

@medications.route("/medications/dopamine")
def dopamine():

    keys = get_key_list()
    session['path'] = 'medications.dopamine'
    return render_template('/medications/dopamine.html', keys=keys, varTitle="Dopamine")

@medications.route("/medications/droperidol")
def droperidol():

    keys = get_key_list()
    session['path'] = 'medications.droperidol'
    return render_template('/medications/droperidol.html', keys=keys, varTitle="Droperidol")

@medications.route("/medications/epinephrine")
def epinephrine():

    keys = get_key_list()
    session['path'] = 'medications.epinephrine'
    return render_template('/medications/epinephrine.html', keys=keys, varTitle="Epinephrine")

@medications.route("/medications/fentanyl")
def fentanyl():

    keys = get_key_list()
    session['path'] = 'medications.fentanyl'
    return render_template('/medications/fentanyl.html', keys=keys, varTitle="Fentanyl")

@medications.route("/medications/glucagon")
def glucagon():

    keys = get_key_list()
    session['path'] = 'medications.glucagon'
    return render_template('/medications/glucagon.html', keys=keys, varTitle="Glucagon")

@medications.route("/medications/glucose")
def glucose():
    
    keys = get_key_list()  
    session['path'] = 'medications.glucose'
    return render_template('/medications/glucose.html', keys=keys, varTitle="Glucose")

@medications.route("/medications/ibuprophen")
def ibuprophen():
    
    keys = get_key_list()  
    session['path'] = 'medications.ibuprophen'
    return render_template('/medications/ibuprophen.html', keys=keys, varTitle="Ibuprophen")

@medications.route("/medications/ketamine")
def ketamine():
    
    keys = get_key_list()  
    session['path'] = 'medications.ketamine'
    return render_template('/medications/ketamine.html', keys=keys, varTitle="Ketamine")

@medications.route("/medications/labetalol")
def labetalol():
    
    keys = get_key_list()  
    session['path'] = 'medications.labetalol'
    return render_template('/medications/labetalol.html', keys=keys, varTitle="Labetalol")

@medications.route("/medications/lidocaine")
def lidocaine():
    
    keys = get_key_list()  
    session['path'] = 'medications.lidocaine'
    return render_template('/medications/lidocaine.html', keys=keys, varTitle="Lidocaine")

@medications.route("/medications/magnesium")
def magnesium():
    
    keys = get_key_list()  
    session['path'] = 'medications.magnesium'
    return render_template('/medications/magnesium.html', keys=keys, varTitle="Magnesium")

@medications.route("/medications/midazolam")
def midazolam():
    
    keys = get_key_list()  
    session['path'] = 'medications.midazolam'
    return render_template('/medications/midazolam.html', keys=keys, varTitle="Midazolam")

@medications.route("/medications/naloxone")
def naloxone():
    
    keys = get_key_list()  
    session['path'] = 'medications.naloxone'
    return render_template('/medications/naloxone.html', keys=keys, varTitle="Naloxone")

@medications.route("/medications/nitroglycerin")
def nitroglycerin():
    
    keys = get_key_list()  
    session['path'] = 'medications.nitroglycerin'
    return render_template('/medications/nitroglycerin.html', keys=keys, varTitle="Nitroglycerin")

@medications.route("/medications/nitrous")
def nitrous():
    
    keys = get_key_list()  
    session['path'] = 'medications.nitrous'
    return render_template('/medications/nitrous.html', keys=keys, varTitle="Nitrous")

@medications.route("/medications/norepinephrine")
def norepinephrine():
    
    keys = get_key_list()  
    session['path'] = 'medications.norepinephrine'
    return render_template('/medications/norepinephrine.html', keys=keys, varTitle="Norepinephrine")

@medications.route("/medications/ondansetron")
def ondansetron():
    
    keys = get_key_list()  
    session['path'] = 'medications.ondansetron'
    return render_template('/medications/ondansetron.html', keys=keys, varTitle="Ondansetron")

@medications.route("/medications/bicarb")
def bicarb():    
    
    keys = get_key_list()
    session['path'] = 'medications.bicarb'
    return render_template('/medications/bicarb.html', keys=keys, varTitle="Sodium Bicarb")

@medications.route("/medications/sodium_thiosulfate")
def sodiumThiosulfate():    
    
    keys = get_key_list()
    session['path'] = 'medications.sodiumThiosulfate'
    return render_template('/medications/sodium_thiosulfate.html', keys=keys, varTitle="Sodium Thiosulfate")