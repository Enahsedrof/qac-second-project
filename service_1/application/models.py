from application import db
from flask_wtf import FlaskForm
from wtforms import SubmitField

class workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(10), nullable = False)
    reps = db.Column(db.Integer, nullable = False)

class GenerateWorkout(FlaskForm):
    submit = SubmitField('Workout')