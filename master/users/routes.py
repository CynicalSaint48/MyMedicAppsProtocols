# users/routes.py

from flask import render_template, request, Blueprint, redirect, url_for, session, flash
from decimal import *
from master.users.forms import RegistrationForm, LoginForm, AccountForm
from master import db, bcrypt
from master.models import User, UpdatePost
from flask_login import login_user, logout_user, login_required, current_user


users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created!', 'message_success')
        return redirect(url_for('users.login'))
    
    return render_template('register.html', varTitle='Register', form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user= User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful.  Please check your email and password', 'danger')        
    
    return render_template('login.html', varTitle='Login', form=form)

@users.route("/logout")
def logout():
        logout_user()
        return redirect(url_for('main.home'))

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = AccountForm()
    if form.validate_on_submit():
        current_user.displayName = form.displayName.data
        current_user.showNarrative = form.showNarrative.data
        current_user.showBasic = form.showBasic.data
        current_user.showAdvanced = form.showAdvanced.data
        current_user.showAdditional = form.showAdditional.data
        db.session.commit()
        flash('Your Account has been updated!', 'message_success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.displayName.data = current_user.displayName
        form.showNarrative.data = current_user.showNarrative
        form.showBasic.data = current_user.showBasic
        form.showAdvanced.data = current_user.showAdvanced
        form.showAdditional.data = current_user.showAdditional

    return render_template('account.html', varTitle='Account', form=form)