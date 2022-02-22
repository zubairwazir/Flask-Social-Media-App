from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class ProfileFootball(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(min=3, max =20), unique= True)
    running_speed = db.Column(db.String(min=1, max=2))
    passing_ability =db.Column(db.String(min=4, max=20))
    level_status =db.Column(db.String(min=5, max=12))
    age = db.Column(db.Integer(min=2, max=2), nullable = False)
    race = db.Column(db.String(min=3, max =12), nullable = False)
    height = db.Column(db.String(min=2, max=2), nullable = False)
    weight =db.Column(db.Integer(min=2, max=3))

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
