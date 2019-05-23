from flask import Blueprint

user_app = Blueprint('user', __name__)

@user_app.route('/login')
def login():
  return '<h1>login</h1>'