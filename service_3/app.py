from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/getreps', methods= ["GET"])
def rep():
    return jsonify(random.randint(1,15))

if __name__=="__main__": app.run(port=5002, host='0.0.0.0', debug=True)  