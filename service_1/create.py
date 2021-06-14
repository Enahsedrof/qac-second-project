from application import db
from application.models import workout


db.drop_all()
db.create_all()