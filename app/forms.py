from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, DateField, PasswordField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, NumberRange, Email, Length, IPAddress, EqualTo, InputRequired

class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[Email()])
    gender = RadioField('gender', choices=[("m", "M"), ("f", "F")])
    age = IntegerField('age', validators=[DataRequired(), NumberRange(18, 100)])
    created = DateField('created')
    password = PasswordField('password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    IPv4 = StringField('IPv4', validators=[IPAddress(ipv4=True, ipv6=False, message=None)])
    profs = SelectMultipleField('profs', choices=[('qa', 'QA'), ('dev', 'Developer'), ('sales', 'Sales')], option_widget=None)
