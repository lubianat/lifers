from app import db
from flask_login import UserMixin


# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)
#     observations = db.relationship("Observation", backref="observer", lazy=True)


class Observation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity_global_id = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(120), nullable=True)
    notes = db.Column(db.String(500), nullable=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    list_id = db.Column(
        db.Integer, db.ForeignKey("observation_list.id"), nullable=False
    )


class ObservationList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(120), nullable=False)
    observations = db.relationship("Observation", backref="observation_list", lazy=True)
