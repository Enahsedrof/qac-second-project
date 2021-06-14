from flask import Flask
import random

app = Flask(__name__)

exercises = ["Press ups", "Push ups", "Sit ups", "Star Jumps", "Binge TV"]

@app.route('/getexercises', methods= ["GET"])
def exer():
    return random.choice(exercises)

if __name__=="__main__": app.run(port=5001, host='0.0.0.0', debug=True)  