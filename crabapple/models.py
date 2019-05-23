from .extensions import db
from datetime import datetime

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  password_hash = db.Column(db.String(128))
  create_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)

class Article(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100))
  content = db.Column(db.Text)
  create_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)
  modify_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
