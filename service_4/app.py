  
from flask import redirect, url_for, request, jsonify, Flask
import random, requests

app = Flask(__name__)

@app.route('/kcal', methods = ['GET', 'POST'])
def calculatekcal():
    rep_number = request.json["dnum"]
    exercise = request.json["exer"]

    
    for i in range (8):
        if exercise ==  "Binge TV":
            fake_kcal = "Nice try, Tv is not exercise"
        
        else:
            kcal = "Nice going, you burned over 100 Calories"

    info = {"exercise": exercise, "rep_number": rep_number, "fake_kcal": fake_kcal, "kcal": kcal } 
    return jsonify(info)

if __name__=="__main__": app.run(port=5003, host='0.0.0.0', debug=True)  