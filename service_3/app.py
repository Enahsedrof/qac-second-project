from flask import Flask, jsonify
import random
app = Flask(__name__)

exercise = ["Press ups", "Sits ups", "Pull ups"]

@app.route('/get_exercise', methods=['GET'])
def get_exercise():
    return jsonify(random.choice(exercise))

if __name__ == '__main__': app.run(host='0.0.0.0', port = 5000, debug=True)