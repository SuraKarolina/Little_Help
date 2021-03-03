from app import db
from app.models import User, Post

db.drop_all()
db.create_all()

db_data = User(id = db.Column(db.Integer, primary_key=True),
username = db.Column(db.String(50), unique=True, nullable=False),
email = db.Column(db.String(120), unique=True, nullable=False),
location = db.Column(db.String(50), unique=False, nullable=False),
password = db.Column(db.String(60), nullable=False),
posts = db.relationship('Post', backref='author', lazy=True)),
Post(id = db.Column(db.Integer, primary_key=True),
title = db.Column(db.String(100), nullable=False),
date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow),
content = db.Column(db.Text, nullable=False),
user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False),
reward = db.Column(db.String(50), nullable=False))
db.session.add(db_data)
db.session.commit()