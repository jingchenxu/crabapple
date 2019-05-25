from flask import Flask, render_template

from .blueprints.article import article_app
from .blueprints.user import user_app
from .blueprints.interceptor import interceptor_app

from .extensions import db, bootstrap

from .settings import config

import os

import click

# TIP db.create_all 需要在引入类的前提下
from .models import User, Article

def create_app(config_name=None):
  '''
  创建应用实例
  '''
  app = Flask('crabapple')
  '''
  加载配置文件
  '''
  if config_name is None:
    config_name = os.getenv('FLASK_CONFIG', 'development')

  app.config.from_object(config[config_name])
  register_blueprints(app)
  register_errors(app)
  register_commands(app)
  register_extensions(app)
  return app

def register_blueprints(app):
  '''
  将蓝图注册到应用实例当中
  '''
  app.register_blueprint(article_app, url_prefix='/article')
  app.register_blueprint(user_app, url_prefix='/user')
  app.register_blueprint(interceptor_app)

def register_extensions(app):
  '''
  注册插件
  '''
  db.init_app(app)
  bootstrap.init_app(app)

def register_errors(app):
  '''
  注册异常处理机制
  '''
  @app.errorhandler(404)
  def page_not_found(e):
    return render_template('404.html')

  @app.errorhandler(400)
  def bad_request(e):
    return render_template('400.html')

  @app.errorhandler(500)
  def internal_server_error(e):
    return render_template('500.html')

def register_commands(app):
  '''
  初始化数据库
  '''
  @app.cli.command()
  def init():
    '''
    初始化数据库
    '''
    click.echo('Initializing the database...')
    db.create_all()
    db.session.commit()
    click.echo('Done')
  '''
  初始化基础数据
  '''
  @app.cli.command()
  def forge():
    '''初始化基础数据'''
    db.drop_all()
    db.create_all()

    click.echo('Done')