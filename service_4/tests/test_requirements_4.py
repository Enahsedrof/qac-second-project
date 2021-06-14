from flask_testing import TestCase
from flask import url_for
from app import app, calculatekcal

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_service_4(self):
        exercise = "Press ups"
        rep = 10
        senditems = {"dnum": rep, "exer": exercise}
        info = self.client.post(url_for("calculatekcal"), json=senditems).json
        print(info)
        print("Testing variables")
        
        
        self.assertIn("fake_kcal",str(info))
    
    def test_service4_again(self):
        exercise = "Press ups"
        rep = 5
        senditems = {"dnum": rep, "exer": exercise}
        info = self.client.post(url_for("calculatekcal"), json=senditems).json
        
        
        self.assertIn("kcal",str(info))