from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired
from wtforms.widgets import TextArea


class AddPetForm(FlaskForm):

    name = StringField("Pet name:")
    species = StringField("Species:")
    photo = StringField("Photo URL:")
    age = SelectField('Age:',  choices=[('baby', 'Baby'), ('young', 'Young'), 
                                        ('adult', 'Adult'), ('senior', 'Senior'), ('dead', 'Dead')])
    note = TextAreaField('Notes:', widget=TextArea())