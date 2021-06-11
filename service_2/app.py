from flask import Flask, jsonify
import random

app = Flask(__name__)



@app.route('/get_rep', methods=['GET'])
def get_rep():
    return jsonify(random.randint(1,20))

if __name__ == '__main__': app.run(host='0.0.0.0', port = 5001, debug=True)