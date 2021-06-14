  
from flask import render_template, request, url_for, Response, jsonify, json
from application import app, db
from application.models import workout, GenerateWorkout
from sqlalchemy import desc
import random, requests
import os

app.config['SECRET_KEY'] = "erhaetrha"

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = GenerateWorkout()

    if form.validate_on_submit():
        rep_number = requests.get('http://service_3:5002/getreps').json()
        exercise = requests.get('http://service_2:5001/getexercises').text

        senditems = {"dnum": rep_number, "exer": exercise}
        info = requests.post("http://service_4:5003/kcal", json=senditems).json()

        new_workout = workout(
            exercise = info["exercise"],
            rep_number = info["rep_number"]
            )
        db.session.add(new_workout)
        db.session.commit()
        
        last_workout = workout.query.order_by(desc(workout.id)).limit(5).all()
        
        return render_template('index.html', title='Workout', form = form, info=info, last_workout = last_workout)
    return render_template('index.html', title='Workout', form = form)