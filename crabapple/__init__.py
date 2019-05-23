from flask import Flask

from .blueprints.article import article_app
from .blueprints.user import user_app
from .blueprints.excepition import exception_app
from .blueprints.interceptor import interceptor_app

from .extensions import db

from .settings import config

import os

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
  return app

def register_blueprints(app):
  '''
  将蓝图注册到应用实例当中
  '''
  app.register_blueprint(article_app, url_prefix='/article')
  app.register_blueprint(user_app, url_prefix='/user')
  app.register_blueprint(exception_app)
  app.register_blueprint(interceptor_app)

def register_extensions(app):
  '''
  注册插件
  '''
  db.init_app(app)
  