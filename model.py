"""Models for Melon Tasting Scheduler App"""

#import the SQLAlchemy constructor function
from flask_sqlalchemy import SQLAlchemy

#delete the below line after creating the server
from flask import (Flask, render_template, request, flash, session, redirect, jsonify)

#calling the constructor function, creating an instance of 
#SQLAlchemy & assigning it to the variable "db"
db = SQLAlchemy()

app = Flask(__name__) #delete after you set up the server

class User(db.Model):
    """A user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)

    def __repr__(self):
        return f"<User user_id={self.user_id} username={self.username} email={self.email}>"


class Reservation(db.Model):
    """A reservation"""

    __tablename__ = 'reservations'


def connect_to_db(flask_app, db_uri="postgresql:///reservations", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == '__main__':

    connect_to_db(app)
