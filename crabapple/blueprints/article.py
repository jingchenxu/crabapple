from flask import Blueprint, render_template
from crabapple.models import Article

article_app = Blueprint('article', __name__)

@article_app.route('/getarticlelist')
def get_article_list():
  return '<h1>获取文章列表</h1>'

@article_app.route('/getarticledetail/<int:id>')
def get_article_detail(id):
  print('文章编号 {}'.format(id))
  return render_template('get_article_detail.html')

@article_app.route('addarticle')
def add_article():
  print('跳转到文章新增页面')
  return render_template('add_article.html')