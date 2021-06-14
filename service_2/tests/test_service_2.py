from flask_testing import TestCase
from flask import url_for
from app import app, exer

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_service_2(self):
        
        response = self.client.get(url_for("exer"))

        exercises = ["Press ups", "Push ups", "Sit ups", "Star Jumps", "Binge TV"]
        self.assertIn(response.data.decode(), exercises)