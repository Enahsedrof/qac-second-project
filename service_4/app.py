from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post_kcals', methods=['POST', 'GET'])
def post_kcals():
    rep = request.json['rep']
    exercise = request.json['exercise']

    kcal = rep * 10

    return jsonify(kcal)

if __name__ == '__main__': app.run(host='0.0.0.0', port = 5003, debug=True)