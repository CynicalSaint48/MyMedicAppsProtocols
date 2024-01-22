# main/routes.py
from flask import render_template, request, Blueprint, redirect, url_for, session
from decimal import *
from master.users.forms import updatePtForm
from flask_login import login_user, logout_user, login_required, current_user
from master.models import UpdatePost
from master.protocols.routes import get_key_list


main = Blueprint('main', __name__)




def getPt():

    keys= {}
    
    if not session.get('ptYears'):
        session['ptYears'] = 0
        session['ptLbs'] = 0.0
        session['ptKgs'] = 0.0
        keys['ptYears'] = 0
        keys['ptLbs'] = 0.0
        keys['ptKgs'] = 0.0
    
    if ( session['ptYears'] == 0.0):
        keys = setPt()
        ptYears = keys['ptYears']
        ptLbs = keys['ptLbs']
        ptKgs = keys['ptKgs']

    else:
        ptYears = session['ptYears']
        ptLbs = session['ptLbs']
        ptKgs = session['ptKgs']
        keys['ptYears'] = ptYears
        keys['ptLbs'] = ptLbs
        keys['ptKgs'] = ptKgs
    
    return keys

def setPt(years=0, lbs=0):
    session['ptYears'] = years
    session['ptLbs'] = lbs
    session['ptKgs'] = round((lbs/2.2), 1)
    
    
    ptYears = session['ptYears']
    ptLbs = session['ptLbs']
    ptKgs = Decimal(session['ptKgs'])
    ptKgs = session['ptKgs']

    keys = {'ptYears':0, 'ptKgs':0.0, 'ptLbs':0}
    keys['ptYears'] = ptYears
    keys['ptKgs'] = ptKgs
    keys['ptLbs'] = ptLbs
    
    return keys



@main.route("/")
@main.route("/home")
def home():

    keys = getPt()
    session['path'] = 'main.home'
    latest_update = UpdatePost.query.order_by(UpdatePost.date_posted.desc()).first()
    if current_user.is_authenticated:
        return render_template('home.html', varTitle='Home', keys=keys, latest_update=latest_update)
    else:
        return redirect(url_for('users.login'))
    


@main.route("/clrPt")
def clrPt():
    session['ptYears'] = 0
    session['ptLbs'] = 0.0
    session['ptKgs'] = 0.0    
    latest_update = UpdatePost.query.order_by(UpdatePost.date_posted.desc()).first()   

    keys = setPt()

    if session['path']:
        path = session['path']
        return redirect(url_for(f'{path}'))
        
    else:

        return redirect(url_for('main.home'))

@main.route("/updatePt", methods=['GET', 'POST'])
def updatePt():
    latest_update = UpdatePost.query.order_by(UpdatePost.date_posted.desc()).first()
    keys = getPt()
    form = updatePtForm()
    if form.validate_on_submit():
        setPt(form.ptYears.data, form.ptLbs.data)

        if session['path']:
            path = session['path']
            return redirect(url_for(f'{path}'))
        
        else:

            return redirect(url_for('main.home'))
    
    return render_template('updatePt.html', varTitle='Add Patient', form=form, legend='New Patient', subButton='Save', latest_update=latest_update, keys=keys)


@main.route("/site_updates", methods=['GET', 'POST'])
def siteUpdates():

    updates = UpdatePost.query.order_by(UpdatePost.date_posted.desc())
    keys = getPt()

    return render_template('site_updates.html', varTitle='Updates', updates=updates, keys=keys)
