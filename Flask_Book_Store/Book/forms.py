from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, validators
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=1,max=20)])
    email = EmailField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
