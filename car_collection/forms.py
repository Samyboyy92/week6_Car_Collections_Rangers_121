from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    username = StringField('username', validators= [DataRequired()])
    email = StringField('email', validators= [DataRequired(), Email()])
    password = PasswordField('password', validators = [DataRequired()])
    submit_button = SubmitField()


class CarForm(FlaskForm):
    color = StringField('color')
    year = StringField('year')
    make = StringField('make')
    model = StringField('model')
    max_speed = StringField('max speed')
    submit_button = SubmitField()



    