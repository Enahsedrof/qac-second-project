from flask import Flask
import random
app = Flask(__name__)

exercises = ["Press ups","Pull ups","Sit ups","Burpees","Starjumps",]

@app.route('/get_exercise', methods=['GET'])
def get_exercise():
    return (random.choice(exercises))

if __name__ == '__main__': app.run(host='0.0.0.0', port = 5002, debug=True)