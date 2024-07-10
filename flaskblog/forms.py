from flask_wtf  import FlaskForm
from wtforms import StringField, PasswordField, BooleanField , SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)]    ) 
    email = StringField('Email',  validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators= [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')
    
    def validate_username(form, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username taken ! Please choose a  different one.')
    def validate_email(form, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email taken ! Please  choose a different one.')
    
class LoginForm(FlaskForm):
    email = StringField('Email',  validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators= [DataRequired()])
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login')
    
    
    