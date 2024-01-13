from flask import render_template, Blueprint
from flask import session, request

protocols = Blueprint('protocols', __name__)

def get_key_list():

    keys={'ptYears':0, 'ptKgs':0.0, 'ptAdult':'', 'ptYears7':'', 'ptYears14':'',
           'ptMax5':'', 'ptMax20':'', 'ptMax26':'', 'ptMax30':'', 'ptMax33':'', 'ptMax37':'',
             'ptMax40':'', 'ptMax43':'', 'ptMax50':'', 'ptMax66':'', 'ptMax75':'', 'ptMax80':'',
               'ptMax100':'', 'ptMax120':'', 'ptMax200':'', 'ptMax300':''}

    if not session['ptYears']:
        ptYears = 0
        keys['ptYears'] = 0
        ptKgs = 0.0
        keys['ptKgs'] = 0.0

    elif session['ptYears'] == '':
        ptYears = 0
        keys['ptYears'] = 0
        ptKgs = 0.0
        keys['ptKgs'] = 0.0

    else:
        ptYears = session['ptYears']
        keys['ptYears'] = ptYears
        ptKgs = session['ptKgs']
        keys['ptKgs'] = ptKgs

    if ptYears >= 18:
        keys['ptYears7'] = True
        keys['ptYears14'] = True
        keys['ptAdult'] = True

    elif ptYears > 14:
        keys['ptYears7'] = True
        keys['ptYears14'] = True
        keys['ptAdult'] = False

    elif ptYears > 7:
        keys['ptYears7'] = True
        keys['ptYears14'] = False
        keys['ptAdult'] = False

    else:
        keys['ptYears7'] = False
        keys['ptYears14'] = False
        keys['ptAdult'] = False

    if ptKgs >= 300:
        keys['ptMax5']= True
        keys['ptMax20'] = True
        keys['ptMax26'] = True
        keys['ptMax30'] = True
        keys['ptMax33'] = True
        keys['ptMax37'] = True
        keys['ptMax40'] = True
        keys['ptMax43'] = True
        keys['ptMax50'] = True
        keys['ptMax66'] = True
        keys['ptMax75'] = True
        keys['ptMax80'] = True
        keys['ptMax100'] = True
        keys['ptMax120'] = True
        keys['ptMax200'] = True
        keys['ptMax300'] = True

    elif ptKgs >= 200:
        keys['ptMax5']= True
        keys['ptMax20'] = True
        keys['ptMax26'] = True
        keys['ptMax30'] = True
        keys['ptMax33'] = True
        keys['ptMax37'] = True
        keys['ptMax40'] = True
        keys['ptMax43'] = True
        keys['ptMax50'] = True
        keys['ptMax66'] = True
        keys['ptMax75'] = True
        keys['ptMax80'] = True
        keys['ptMax100'] = True
        keys['ptMax120'] = True
        keys['ptMax200'] = True
        keys['ptMax300'] = False

    elif ptKgs >= 120:
        keys['ptMax5']= True
        keys['ptMax20'] = True
        keys['ptMax26'] = True
        keys['ptMax30'] = True
        keys['ptMax33'] = True
        keys['ptMax37'] = True
        keys['ptMax40'] = True
        keys['ptMax43'] = True
        keys['ptMax50'] = True
        keys['ptMax66'] = True
        keys['ptMax75'] = True
        keys['ptMax80'] = True
        keys['ptMax100'] = True
        keys['ptMax120'] = True
        keys['ptMax200'] = False
        keys['ptMax300'] = False

    elif ptKgs >= 100:
        keys['ptMax5']= True
        keys['ptMax20'] = True
        keys['ptMax26'] = True
        keys['ptMax30'] = True
        keys['ptMax33'] = True
        keys['ptMax37'] = True
        keys['ptMax40'] = True
        keys['ptMax43'] = True
        keys['ptMax50'] = True
        keys['ptMax66'] = True
        keys['ptMax75'] = True
        keys['ptMax80'] = True
        keys['ptMax100'] = True
        keys['ptMax120'] = False
        keys['ptMax200'] = False
        keys['ptMax300'] = False

    elif ptKgs >= 80:
        keys['ptMax5']= True
        keys['ptMax20'] = True
        keys['ptMax26'] = True
        keys['ptMax30'] = True
        keys['ptMax33'] = True
        keys['ptMax37'] = True
        keys['ptMax40'] = True
        keys['ptMax43'] = True
        keys['ptMax50'] = True
        keys['ptMax66'] = True
        keys['ptMax75'] = True
        keys['ptMax80'] = True
        keys['ptMax100'] = False
        keys['ptMax120'] = False
        keys['ptMax200'] = False
        keys['ptMax300'] = False

    elif ptKgs >= 75:
        keys['ptMax5']= True
        keys['ptMax20'] = True
        keys['ptMax26'] = True
        keys['ptMax30'] = True
        keys['ptMax33'] = True
        keys['ptMax37'] = True
        keys['ptMax40'] = True
        keys['ptMax43'] = True
        keys['ptMax50'] = True
        keys['ptMax66'] = True
        keys['ptMax75'] = True
        keys['ptMax80'] = False
        keys['ptMax100'] = False
        keys['ptMax120'] = False
        keys['ptMax200'] = False
        keys['ptMax300'] = False

    elif ptKgs >= 66:
        keys['ptMax5']= True
        keys['ptMax20'] = True
        keys['ptMax26'] = True
        keys['ptMax30'] = True
        keys['ptMax33'] = True
        keys['ptMax37'] = True
        keys['ptMax40'] = True
        keys['ptMax43'] = True
        keys['ptMax50'] = True
        keys['ptMax66'] = True
        keys['ptMax75'] = False
        keys['ptMax80'] = False
        keys['ptMax100'] = False
        keys['ptMax120'] = False
        keys['ptMax200'] = False
        keys['ptMax300'] = False

    elif ptKgs >= 50:
        keys['ptMax5']= True
        keys['ptMax20'] = True
        keys['ptMax26'] = True
        keys['ptMax30'] = True
        keys['ptMax33'] = True
        keys['ptMax37'] = True
        keys['ptMax40'] = True
        keys['ptMax43'] = True
        keys['ptMax50'] = True
        keys['ptMax66'] = False
        keys['ptMax75'] = False
        keys['ptMax80'] = False
        keys['ptMax100'] = False
        keys['ptMax120'] = False
        keys['ptMax200'] = False
        keys['ptMax300'] = False

    elif ptKgs >= 43:
        keys['ptMax5']= True
        keys['ptMax20'] = True
        keys['ptMax26'] = True
        keys['ptMax30'] = True
        keys['ptMax33'] = True
        keys['ptMax37'] = True
        keys['ptMax40'] = True
        keys['ptMax43'] = True
        keys['ptMax50'] = False
        keys['ptMax66'] = False
        keys['ptMax75'] = False
        keys['ptMax80'] = False
        keys['ptMax100'] = False
        keys['ptMax120'] = False
        keys['ptMax200'] = False
        keys['ptMax300'] = False

    elif ptKgs >= 40:
        keys['ptMax5']= True
        keys['ptMax20'] = True
        keys['ptMax26'] = True
        keys['ptMax30'] = True
        keys['ptMax33'] = True
        keys['ptMax37'] = True
        keys['ptMax40'] = True
        keys['ptMax43'] = False
        keys['ptMax50'] = False
        keys['ptMax66'] = False
        keys['ptMax75'] = False
        keys['ptMax80'] = False
        keys['ptMax100'] = False
        keys['ptMax120'] = False
        keys['ptMax200'] = False
        keys['ptMax300'] = False

    elif ptKgs >= 37:
        keys['ptMax5']= True
        keys['ptMax20'] = True
        keys['ptMax26'] = True
        keys['ptMax30'] = True
        keys['ptMax33'] = True
        keys['ptMax37'] = True
        keys['ptMax40'] = False
        keys['ptMax43'] = False
        keys['ptMax50'] = False
        keys['ptMax66'] = False
        keys['ptMax75'] = False
        keys['ptMax80'] = False
        keys['ptMax100'] = False
        keys['ptMax120'] = False
        keys['ptMax200'] = False
        keys['ptMax300'] = False

    elif ptKgs >= 33:
        keys['ptMax5']= True
        keys['ptMax20'] = True
        keys['ptMax26'] = True
        keys['ptMax30'] = True
        keys['ptMax33'] = True
        keys['ptMax37'] = False
        keys['ptMax40'] = False
        keys['ptMax43'] = False
        keys['ptMax50'] = False
        keys['ptMax66'] = False
        keys['ptMax75'] = False
        keys['ptMax80'] = False
        keys['ptMax100'] = False
        keys['ptMax120'] = False
        keys['ptMax200'] = False
        keys['ptMax300'] = False

    elif ptKgs >= 30:
        keys['ptMax5']= True
        keys['ptMax20'] = True
        keys['ptMax26'] = True
        keys['ptMax30'] = True
        keys['ptMax33'] = False
        keys['ptMax37'] = False
        keys['ptMax40'] = False
        keys['ptMax43'] = False
        keys['ptMax50'] = False
        keys['ptMax66'] = False
        keys['ptMax75'] = False
        keys['ptMax80'] = False
        keys['ptMax100'] = False
        keys['ptMax120'] = False
        keys['ptMax200'] = False
        keys['ptMax300'] = False

    elif ptKgs >= 26:
        keys['ptMax5']= True
        keys['ptMax20'] = True
        keys['ptMax26'] = True
        keys['ptMax30'] = False
        keys['ptMax33'] = False
        keys['ptMax37'] = False
        keys['ptMax40'] = False
        keys['ptMax43'] = False
        keys['ptMax50'] = False
        keys['ptMax66'] = False
        keys['ptMax75'] = False
        keys['ptMax80'] = False
        keys['ptMax100'] = False
        keys['ptMax120'] = False
        keys['ptMax200'] = False
        keys['ptMax300'] = False

    elif ptKgs >= 20:
        keys['ptMax5']= True
        keys['ptMax20'] = True
        keys['ptMax26'] = False
        keys['ptMax30'] = False
        keys['ptMax33'] = False
        keys['ptMax40'] = False
        keys['ptMax43'] = False
        keys['ptMax50'] = False
        keys['ptMax66'] = False
        keys['ptMax75'] = False
        keys['ptMax80'] = False
        keys['ptMax100'] = False
        keys['ptMax120'] = False
        keys['ptMax200'] = False
        keys['ptMax300'] = False

    elif ptKgs >= 5:
        keys['ptMax5']= True
        keys['ptMax20'] = False
        keys['ptMax26'] = False
        keys['ptMax30'] = False
        keys['ptMax33'] = False
        keys['ptMax40'] = False
        keys['ptMax43'] = False
        keys['ptMax50'] = False
        keys['ptMax66'] = False
        keys['ptMax75'] = False
        keys['ptMax80'] = False
        keys['ptMax100'] = False
        keys['ptMax120'] = False
        keys['ptMax200'] = False
        keys['ptMax300'] = False

    else:
        keys['ptMax5']= False
        keys['ptMax20'] = False
        keys['ptMax26'] = False
        keys['ptMax30'] = False
        keys['ptMax33'] = False
        keys['ptMax40'] = False
        keys['ptMax43'] = False
        keys['ptMax50'] = False
        keys['ptMax66'] = False
        keys['ptMax75'] = False
        keys['ptMax80'] = False
        keys['ptMax100'] = False
        keys['ptMax120'] = False
        keys['ptMax200'] = False
        keys['ptMax300'] = False

    return (keys)

@protocols.route("/protocols/allergic_reaction")
def allergy():

    keys = get_key_list()
    session['path'] = 'protocols.allergy'
    return render_template('/protocols/AllergicReaction.html', keys=keys, varTitle="Allergic Reaction")

@protocols.route("/protocols/abdominal_pain")
def abdominal():

    keys = get_key_list()
    session['path'] = 'protocols.abdominal'

    return render_template('/protocols/AbdPain.html', keys=keys, varTitle="Abdominal Pain")

@protocols.route("/protocols/bites_envenomations")
def bites():

    keys = get_key_list()
    session['path'] = 'protocols.bites'

    return render_template('/protocols/Bites_Envenomations.html', keys=keys, varTitle="Bites & Envenomations")

@protocols.route("/protocols/animal_bites")
def animalBites():

    keys = get_key_list()
    session['path'] = 'protocols.animalBites'

    return render_template('/protocols/AnimalBites.html', keys=keys, varTitle="Animal Bites")

@protocols.route("/protocols/assault")
def assault():

    keys = get_key_list()
    session['path'] = 'protocols.assault'

    return render_template('/protocols/Assault.html', keys=keys, varTitle="Assault")

@protocols.route("/protocols/BackPain")
def backPain():

    keys = get_key_list()
    session['path'] = 'protocols.backPain'

    return render_template('/protocols/BackPain.html', keys=keys, varTitle="Back Pain")

@protocols.route("/protocols/BreathingProblems")
def breathingProblems():

    keys = get_key_list()
    session['path'] = 'protocols.breathingProblems'

    return render_template('/protocols/BreathingProblems.html', keys=keys, varTitle="Breathing Problems")

@protocols.route("/protocols/Burns")
def burns():

    keys = get_key_list()
    session['path'] = 'protocols.burns'

    return render_template('/protocols/Burns.html', keys=keys, varTitle="Burns")

@protocols.route("/protocols/HazMat")
def hazmat():

    keys = get_key_list()
    session['path'] = 'protocols.hazmat'

    return render_template('/protocols/CarbonMonoxide.html', keys=keys, varTitle="Hazardous Materials")

@protocols.route("/protocols/CardiacArrest")
def cardiacArrest():

    keys = get_key_list()
    session['path'] = 'protocols.cardiacArrest'

    return render_template('/protocols/CardiacArrest.html', keys=keys, varTitle="Cardiac Arrest")

@protocols.route("/protocols/ChestPain")
def chestPain():

    keys = get_key_list()
    session['path'] = 'protocols.chestPain'

    return render_template('/protocols/ChestPain.html', keys=keys, varTitle="Chest Pain")

@protocols.route("/protocols/Choking")
def choking():

    keys = get_key_list()
    session['path'] = 'protocols.choking'

    return render_template('/protocols/Choking.html', keys=keys, varTitle="Choking")

@protocols.route("/protocols/Convulsions")
def convulsions():

    keys = get_key_list()
    session['path'] = 'protocols.convulsions'

    return render_template('/protocols/Convulsions.html', keys=keys, varTitle="Convulsions/Seizures")

@protocols.route("/protocols/Diabetic")
def diabetic():

    keys = get_key_list()
    session['path'] = 'protocols.diabetic'

    return render_template('/protocols/Diabetic.html', keys=keys, varTitle="Diabetic Problems")

@protocols.route("/protocols/Drowning")
def drowning():

    keys = get_key_list()
    session['path'] = 'protocols.drowning'

    return render_template('/protocols/Drowning.html', keys=keys, varTitle="Drowning")

@protocols.route("/protocols/Electrocution")
def electrocution():

    keys = get_key_list()
    session['path'] = 'protocols.electrocution'

    return render_template('/protocols/Electrocution.html', keys=keys, varTitle="Electrocution")

@protocols.route("/protocols/EyeProblems")
def eyeProblems():

    keys = get_key_list()
    session['path'] = 'protocols.eyeProblems'

    return render_template('/protocols/EyeProblems.html', keys=keys, varTitle="Eye Problems")

@protocols.route("/protocols/Falls")
def falls():

    keys = get_key_list()
    session['path'] = 'protocols.falls'

    return render_template('/protocols/Falls.html', keys=keys, varTitle="Falls /  Back Injury")

@protocols.route("/protocols/Headache")
def headache():

    keys = get_key_list()
    session['path'] = 'protocols.headache'

    return render_template('/protocols/Headache.html', keys=keys, varTitle="Headache")

@protocols.route("/protocols/HeartProblems")
def heartProblems():

    keys = get_key_list()
    session['path'] = 'protocols.heartProblems'

    return render_template('/protocols/HeartProblems.html', keys=keys, varTitle="Heart Problems")

@protocols.route("/protocols/HeatCold")
def heatCold():

    keys = get_key_list()
    session['path'] = 'protocols.heatCold'

    return render_template('/protocols/HeatCold.html', keys=keys, varTitle="Heat/Cold Exposure")

@protocols.route("/protocols/Hemorrhage")
def hemorrhage():

    keys = get_key_list()
    session['path'] = 'protocols.hemorrhage'

    return render_template('/protocols/Hemorrhage.html', keys=keys, varTitle="Hemorrhage")

@protocols.route("/protocols/IndustrialAccident")
def industrial():

    keys = get_key_list()
    session['path'] = 'protocols.industrial'

    return render_template('/protocols/IndustrialAccident.html', keys=keys, varTitle="Industrial Accident")

@protocols.route("/protocols/Overdose")
def overdose():

    keys = get_key_list()
    session['path'] = 'protocols.overdose'

    return render_template('/protocols/Overdose.html', keys=keys, varTitle="Overdose")

@protocols.route("/protocols/PregnancyChildbirth")
def pregnancyChildbirth():

    keys = get_key_list()
    session['path'] = 'protocols.pregnancyChildbirth'

    return render_template('/protocols/PregnancyChildbirth.html', keys=keys, varTitle="PregnancyChildbirth")

@protocols.route("/protocols/Psychiatric")
def psychiatric():

    keys = get_key_list()
    session['path'] = 'protocols.psychiatric'

    return render_template('/protocols/Psychiatric.html', keys=keys, varTitle="Psychiatric")