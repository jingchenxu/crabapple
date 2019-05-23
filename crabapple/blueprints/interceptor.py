from flask import Blueprint

interceptor_app = Blueprint('interceptor', __name__)

@interceptor_app.before_app_first_request
def before_app_first_request():
  '''
  app 接收到第一个请求
  '''
  print('app接收到第一个请求')
  pass

@interceptor_app.before_app_request
def before_app_request():
  '''
  拦截所有的请求
  '''
  print('拦截所有的请求')
  pass

@interceptor_app.after_app_request
def after_app_request(response):
  '''
  请求完成之后
  '''
  print('请求完成之后')
  return response

# @interceptor_app.teardown_app_request
# def teardown_app_request():
#   '''
#   可能会遇到异常
#   '''
#   print('可能会遇到异常')
#   pass