"""forms for notes app"""

from wtforms import StringField, EmailField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email

class RegisterUserForm(FlaskForm):
    """Form for registering users. """

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(max=20)])
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=10, max=100)])
    email = EmailField(
        "Email",
        validators=[InputRequired(), Email(), Length(max=50)])
    first_name = StringField(
        "First Name",
        validators=[InputRequired(),
                    Length(max=30)])
    last_name = StringField("Last Name",
                            validators=Length(max=30))


class LoginForm(FlaskForm):

    """Form for logging in users. """

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(max=20)])
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=10, max=100)])


class CSRFProtectForm(FlaskForm):
    """Form just for CSRF Protection"""