from . import db
from flask_login import UserMixin
from sqlalchemy import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(5000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    blood_pressure = db.Column(db.Integer)
    waist = db.Column(db.Integer)
    bf_percent = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    role = db.Column(db.String(100))
    notes = db.relationship('Note')
    metrics = db.relationship('Metric')