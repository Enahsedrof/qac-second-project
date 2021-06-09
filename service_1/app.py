from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import requests
from os import env

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://data.db' #getenv('DATABASE_URI')
db = SQLAlchemy(app)

class Workouts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    exercise = db.Column(db.String(30), nullable=False)


@app.route('/')
def index():
    rep = requests.get('https://service-2:5000/get/rep').json()
    exercise = requests.get('https://service-3:5000/get/exercise').text

    payload = {'rep': rep, 'exercise': exercise}
    workout = requests.post('https://service-4:5000/post/workout', json=payload).json()
    
    db.session.add(Rep(number = rep, exercise = exercise )
    db.session.commit
    all_workouts= Workouts.query.order_by(desc(Workouts.id)).limit(5).all()

    return render_template("index.html", rep=rep, exercise=exercise, all_workouts=all_workouts)

    # return f"You must do {rep} {exercise} to complete your workout for {workout} calories burned.\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug=True)
