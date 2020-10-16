"""Forms for our demo Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, TextArea
from wtforms.validators import InputRequired, Optional, Email


class AddPetForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Pet name:")
    species = StringField("Species:")
    photo = StringField("Photo URL:")
    age = SelectField('Age:',  choices=[('baby', 'Baby'), ('young', 'Young'), 
                                        ('adult', 'Adult'), ('senior', 'Senior'), ('dead', 'Dead')])
    note = TextAreaField('Notes:', widget=TextArea(row=30, cols=10))


class UserForm(FlaskForm):
    """Form for adding/editing friend."""

    name = StringField("Name",
                       validators=[InputRequired()])
    email = StringField("Email Address",
                        validators=[Optional(), Email()])
