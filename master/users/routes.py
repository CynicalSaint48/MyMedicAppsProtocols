# users/routes.py

from flask import render_template, request, Blueprint, redirect, url_for, session, flash
from decimal import *
from master.users.forms import RegistrationForm, LoginForm

users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account Created for {form.email.data}!', 'message_success')
        return redirect(url_for('main.home'))
    
    return render_template('register.html', varTitle='Register', form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'michaels3@medic911.com' and form.password.data == 'password':
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful.  Please check your email and password', 'danger')
            return redirect(url_for('users.login'))
        
    
    return render_template('login.html', varTitle='Login', form=form)
