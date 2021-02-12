from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email,  EqualTo, ValidationError
from flaskblog.models import User


#Registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)]) #username, can't be empty with 
                                                                                            #min and max length specified
    
    email = StringField('Email',validators=[DataRequired(),Email()]) #email can't be emptyn and has to be valid
    
    password = PasswordField('Password',validators=[DataRequired()]) #password can't be empty
    
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')]) #confirm password can't be empty and has to be 
                                                                                                            #equal to password
    submit = SubmitField('Sign Up') #Submit button
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

    
# Login form     
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember =  BooleanField('remember me')
    submit = SubmitField('Login')
    
class UpdateAccountForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)]) #username, can't be empty with 
                                                                                            #min and max length specified
    
    email = StringField('Email',validators=[DataRequired(),Email()]) #email can't be emptyn and has to be valid
    
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])                                                                                  #equal to password
    submit = SubmitField('Update') #Submit button
    
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')