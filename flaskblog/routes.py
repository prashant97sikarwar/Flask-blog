from flask import render_template, url_for, flash, redirect
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm,  LoginForm
from flaskblog import app

posts = [
    {
        'author' : 'Prashant Sikarwar',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'jan 23,2021'
    },
    {
        'author' : 'sam doew',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'jan 25,2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts = posts)

@app.route("/about")
def about():
    return render_template('about.html',title = 'About')

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Account created for {}!".format(form.username.data), 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in", 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccesful. Please check username or password','danger')
    return render_template('login.html',title='Login',form=form)
