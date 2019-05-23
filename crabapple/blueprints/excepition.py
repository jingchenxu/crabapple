from flask import Blueprint, render_template

exception_app = Blueprint('exception', __name__)

@exception_app.route('/404')
def handle_404():
  return render_template('404.html')