# main/routes.py
from flask import render_template, request, Blueprint, redirect, url_for, session
from decimal import *


main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    if not session:
        session['ptMonths'] = 0.0
        session['ptYears'] = 15.0
        session['ptLbs'] = 0.0
        session['ptKgs'] = 54.5
    
    if (session['ptMonths'] == 0.0 and session['ptYears'] == 0.0):
        ptMonths, ptYears, ptLbs, ptKgs = setPt()
    else:
        ptMonths = session['ptMonths']
        ptYears = session['ptYears']
        ptLbs = session['ptLbs']
        ptKgs = session['ptKgs']

    page = request.args.get('page', 1, type=int)
    return render_template('home.html', varTitle='Home', ptMonths=ptMonths, ptYears=ptYears, ptLbs=ptLbs, ptKgs=ptKgs)

def setPt(months=0, years=0, lbs=0):
    print('Running setPt')
    session['ptMonths'] = months
    session['ptYears'] = years
    session['ptLbs'] = lbs
    session['ptKgs'] = round((lbs/2.2), 1)
    
    if session['ptYears']:
        session['ptMonths'] = 0
    ptMonths = session['ptMonths']
    ptYears = session['ptYears']
    ptLbs = session['ptLbs']
    ptKgs = Decimal(session['ptKgs'])
    ptKgs = session['ptKgs']
    


    return ptMonths, ptYears, ptLbs, ptKgs
