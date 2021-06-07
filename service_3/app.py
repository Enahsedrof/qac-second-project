from flask import Flask 
import random
app = Flask(__name__)

exercise = ["Press ups", "Sits ups", "Pull ups"]

@app.route('/get/exercise')
def get_exercise():
    return random.chose(exercise)

if __name__ == '__main__':
    app.run(host='0.0.0.0')