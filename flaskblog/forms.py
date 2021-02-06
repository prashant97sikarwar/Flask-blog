from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email,  EqualTo

#Registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)]) #username, can't be empty with 
                                                                                            #min and max length specified
    
    email = StringField('Email',validators=[DataRequired(),Email()]) #email can't be emptyn and has to be valid
    
    password = PasswordField('Password',validators=[DataRequired()]) #password can't be empty
    
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')]) #confirm password can't be empty and has to be 
                                                                                                            #equal to password
    submit = SubmitField('Sign Up') #Submit button
    
# Login form     
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember =  BooleanField('remember me')
    submit = SubmitField('Login')
    

