from blog import db
from blog import app
from models import User

with app.app_context():
    print(User.query.all())

