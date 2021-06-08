from flask import Flask, request, jsonify

app = Flask(__name__)

workouts = {
    'exercise': {
        'Press ups' : 15,
        'Sit ups' : 10,
        'Pull ups' : 20
    }
}

@app.route('/post/workout', methods=['POST'])
def post_workout():
    rep = request.json['rep']
    exercise = request.json['exercise']

    workout = workouts['exercise'][exercise] * ['rep'][rep] 

    return jsonify(workout)

if __name__ == '__main__':
    app.run(host ='0.0.0.0')