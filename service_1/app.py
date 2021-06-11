from flask import Flask, render_template, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import requests
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
db = SQLAlchemy(app)

class Workouts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    exercise = db.Column(db.String(30), nullable=False)


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    rep = requests.get("http://service-2:5001/get_rep").json()
    exercise = requests.get("http://service-3:5002/get_exercise").text

    payload = jsonify({'rep': rep, 'exercise': exercise})
    kcal = requests.post('http://service-4:5003/post_kcals', json=payload).json()
    
    db.session.add(Workouts(number = rep, exercise = exercise ))
    db.session.commit()

    all_workouts= Workouts.query.order_by(desc(Workouts.id)).limit(5).all()
    
    return render_template("index.html", rep=rep, exercise=exercise, all_workouts=all_workouts)

if __name__ == '__main__': app.run(host='0.0.0.0', port = 5000, debug=True)
