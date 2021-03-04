from app import db
from app.models import User, Post

db.drop_all()
db.create_all()

