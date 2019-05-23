from flask import Blueprint

article_app = Blueprint('article', __name__)

@article_app.route('/getarticlelist')
def get_article_list():
  return '<h1>获取文章列表</h1>'