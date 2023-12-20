# main/routes.py
from flask import render_template, request, Blueprint, redirect, url_for, session
from decimal import *
from master.users.forms import updatePtForm
from flask_login import login_user, logout_user, login_required, current_user
from master.models import UpdatePost


main = Blueprint('main', __name__)


def getPt():
    if not session.get('ptYears'):
        session['ptYears'] = 0
        session['ptLbs'] = 0.0
        session['ptKgs'] = 0.0
    
    if ( session['ptYears'] == 0.0):
        ptYears, ptLbs, ptKgs = setPt()
    else:
        ptYears = session['ptYears']
        ptLbs = session['ptLbs']
        ptKgs = session['ptKgs']
    
    return ptYears, ptLbs, ptKgs



@main.route("/")
@main.route("/home")
def home():
    
    ptYears = getPt()[0]
    ptKgs = getPt()[2]
    latest_update = UpdatePost.query.order_by(UpdatePost.date_posted.desc()).first()

    return render_template('home.html', varTitle='Home', ptYears=ptYears, ptKgs=ptKgs, latest_update=latest_update)

def setPt(years=0, lbs=0):
    session['ptYears'] = years
    session['ptLbs'] = lbs
    session['ptKgs'] = round((lbs/2.2), 1)
    
    ptYears = session['ptYears']
    ptLbs = session['ptLbs']
    ptKgs = Decimal(session['ptKgs'])
    ptKgs = session['ptKgs']
    
    return ptYears, ptLbs, ptKgs

@main.route("/clrPt")
def clrPt():
    session['ptYears'] = 0
    session['ptLbs'] = 0.0
    session['ptKgs'] = 0.0
    ptYears = session['ptYears']
    ptLbs = session['ptLbs']
    ptKgs = session['ptKgs']

    latest_update = UpdatePost.query.order_by(UpdatePost.date_posted.desc()).first()   

    return render_template('home.html', varTitle='Home', ptYears=ptYears, ptLbs=ptLbs, ptKgs=ptKgs, latest_update=latest_update)

@main.route("/updatePt", methods=['GET', 'POST'])
def updatePt():
    latest_update = UpdatePost.query.order_by(UpdatePost.date_posted.desc()).first()
    form = updatePtForm()
    if form.validate_on_submit():
        setPt(form.ptYears.data, form.ptLbs.data)
        return redirect(url_for('main.home'))
    return render_template('updatePt.html', varTitle='Add Patient', form=form, legend='New Patient', subButton='Save', latest_update=latest_update)


@main.route("/site_updates", methods=['GET', 'POST'])
def siteUpdates():
    updates = UpdatePost.query.order_by(UpdatePost.date_posted.desc())
    ptYears = getPt()[0]
    ptKgs = getPt()[2]

    return render_template('site_updates.html', varTitle='Updates', updates=updates, ptYears=ptYears, ptKgs=ptKgs)
