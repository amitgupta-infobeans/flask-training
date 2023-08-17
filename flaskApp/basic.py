import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate   # pip install Flask-migrate

basedir = os.path.abspath(os.path.dirname(__file__))

# print(basedir)   tells the Absolute path where my file located (basic.py file)

# setup of SqlAlchemy connection...
app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Migrate(app, db)

#---##############################################################

#model name:
class Puppy(db.Model):
    
    # MANUAL TABLE NAME
    __tablename__ = 'puppies'

    # TABLE COLUMNS
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.Text)
    age     = db.Column(db.Integer)
    breed   = db.Column(db.Text)

    # init method
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    # string representation
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old and"
    

