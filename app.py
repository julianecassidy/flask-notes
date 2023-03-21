import os
from flask import Flask, redirect, render_template, session
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User
from forms import RegisterUserForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "very secret key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///notes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.get('/')
def redirect_register():
    """ Redirects to register page """
    return redirect('/register')

@app.get('/register')
def display_register_form():
    """ Show user register form """

    form = RegisterUserForm()

    return render_template('register_user.html', form=form)


@app.post('/register')
def handle_registration_form_submit():
    """ Validate registration form submission; add new user and redirect or re-
    render form"""

    form = RegisterUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data or None

        user = User.register(username, password, email, first_name, last_name)

        db.session.add(user)
        db.session.commit()

        return redirect('/secret')

    else:
        return render_template('register_user.html', form=form)


@app.get('/login')
def display_login_form():
    """ Show login form"""

    form = LoginForm()

    return render_template("login_user.html", form=form)

@app.route('/login', methods=["GET", "POST"])
def process_login_form():
    """Handle user logins"""

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)

        if user:
            session['user_username'] = user.username
            return redirect('/secret')

        else:
            form.username.errors = ["Bad name/password"]

    else:
        return render_template("login_user.html", form=form)


@app.get('/secret')
def display_success_login():
    """return a successful login message"""

    return "You made it!"
