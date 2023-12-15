# users/routes.py

from flask import render_template, request, Blueprint, redirect, url_for, session, flash
from decimal import *
from master.users.forms import RegistrationForm, LoginForm

users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'message_success')
        return redirect(url_for('main.home'))
    
    return render_template('register.html', varTitle='Register', form=form)

@users.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', varTitle='Login', form=form)
