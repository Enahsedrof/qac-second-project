from flask import url_for
from flask_testing import TestCase
from app import app, db
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            DEBUG=True
        )
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestHome(TestBase):
    def test_index_get(self):
        with requests_mock.Mocker() as m:
            m.get(("http://service-2:5000/get_rep").json())
            m.post("http://service-3:5000/get_exercise".json())
            response = self.client.get(url_for("index"))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Do 15 of these Press ups', response.data)
    
    def test_db(self):
        with requests_mock.Mocker() as m:
            test_cases = [(15, "Sit ups"), (10, "Pull ups")]
            for case in test_cases:
                m.get(("http://service-2:5000/get_rep").json(0))
                m.post("http://service-3:5000/get_exercise".json(1))
                response = self.client.get(url_for("index"))
            self.assertIn(b'Do 15 of these Sit ups', response.data)
            self.assertIn(b'Do 10 of these Pull ups', response.data)
            #self.assertIN(response.json['rep'], range(14,17))