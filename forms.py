"""forms for notes app"""

from wtforms import StringField, EmailField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email

class RegisterUserForm(FlaskForm):
    """Form for registering users. """

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=10, max=100)])
    email = EmailField("Email", validators=[InputRequired(), Email()])
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name")


class LoginForm(FlaskForm):

    """Form for logging in users. """

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=10, max=100)])

