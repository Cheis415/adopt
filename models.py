from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False, server_default='')
    age = db.Column(db.Text, db.CheckConstraint("age IN('baby', 'young', 'adult', 'senior', 'dead')"), nullable=False, )
    notes = db.Column(db.Text)    
    available = db.Column(db.Boolean, nullable=False, server_default='true')