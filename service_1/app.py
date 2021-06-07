from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    rep = requests.get('https://service-2:5000/get/rep').text
    exercise = requests.get('https://service-3:5000/get/exercise').text

    payload = {'rep': rep, 'exercise': exercise}
    workout = requests.post('https://service-4:5000/post/workout', json=payload).json

    return f"You must do {rep} {exercise} to complete your workout.\n"