from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from master.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Already Registered, Sign In Below')

class LoginForm(FlaskForm):
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class AccountForm(FlaskForm):
    displayName = StringField('Display Name')
    showNarrative = BooleanField('Show Protocol Narrative', default=1)
    showBasic = BooleanField('Show BLS Treatments', default=1)
    showAdvanced = BooleanField('Show ALS Treatments', default=1)
    showAdditional = BooleanField('Show Additional Info', default=1)
    submit = SubmitField('Update')

class updatePtForm(FlaskForm):
    ptYears = IntegerField('Age in Years',
                            validators=[DataRequired(), NumberRange(min=1, max=105, message='Age Range 1-100; Select 1 for infants.')])
    ptLbs = IntegerField('Weight in Pounds',
                            validators=[DataRequired(), NumberRange(min=1, max=500, message='Weight Range 0 - 500lbs')])
    submit = SubmitField('Save')






    
