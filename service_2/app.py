from flask import Flask, jsonify
import random

app = Flask(__name__)

rep = [5, 10, 15]

@app.route('/get/rep')
def get_rep():
    return jsonify(random.choice(rep))

if __name__ == '__main__':
    app.run(host='0.0.0.0')