from flask_testing import TestCase
from flask import url_for
import requests
from requests_mock import mock
from application import app, db
from application.models import GenerateWorkout

class TestBase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
        app.config['SECRET_KEY'] = "erhaetrha"
        app.config['WTF_CSRF_ENABLED'] = False
        db.drop_all()
        db.create_all()
        return app

class TestResponse(TestBase):
    def test_index(self):
        with mock() as m:
            form = GenerateWorkout
            b = self.client.get(url_for("home"))
            self.assert200(b)
            m.get('http://service_2:5001/getreps', json=10)
            m.get('http://service_3:5002/getexercises', text="Press ups")
            m.post('http://service_4:5003/kcal', json={'exercise': 'Press ups','rep_number': 10})

            response = self.client.post(url_for("home"))

            
            

        self.assert200(response)
        self.assertIn("Press ups", response.data.decode())