from flask import Flask, render_template, redirect
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

from forms import AddPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'BOOO!'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home():
    pets = Pet.query.all()

    return render_template("home.html", pets=pets)


@app.route("/add_pet", methods=["GET", "POST"])
def add_pet():

    

    form = AddPetForm()

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo.data
        pet.age = form.age.data
        pet.notes = form.note.data
        db.session.commit()

        return redirect("/")

    else:
        return render_template("/add_pet.html", form=form)
