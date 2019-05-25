'''
这里是配置文件
'''
import os
import sys

class BaseConfig(object):
  '''
  基本配置文件
  '''
  SECRECT_KEY = os.getenv('SECRECT_KEY', 'dev key')

  SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
  '''
  开发环境配置
  '''
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'dev key')
  pass

class TestingConfig(BaseConfig):
  '''
  测试环境配置
  '''
  pass

class ProductionConfig(BaseConfig):
  '''
  生产环境配置
  '''
  pass

config = {
  'development': DevelopmentConfig,
  'testing': TestingConfig,
  'production': ProductionConfig
}