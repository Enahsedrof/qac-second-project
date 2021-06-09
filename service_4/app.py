from flask import Flask, request, jsonify

app = Flask(__name__)

kcals = {
    'exercise': {
        'Press ups' : 15,
        'Sit ups' : 10,
        'Pull ups' : 20
    }
}

@app.route('/post_kcals', methods=['POST'])
def post_kcals():
    rep = request.json['rep']
    exercise = request.json['exercise']

    kcal = kcals['exercise'][exercise] * ['rep'][rep] 

    return jsonify(kcal)

if __name__ == '__main__': app.run(host='0.0.0.0', port = 5000, debug=True)