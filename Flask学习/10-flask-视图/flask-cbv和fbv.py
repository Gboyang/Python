from flask import Flask, views
import functools
import time

app = Flask(__name__)


def timer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        reg = func(*args, **kwargs)
        print(time.time() - start_time)
        return reg

    return inner


# FBV
# @app.route('/index', methods=['GET', 'POST'])
# @timer
# def index():
#     return 'index'


# CBV的两种写法
# 第一种写法
# class IndexView(views.View):
#     methods = ['GET']
#     decorators = [timer, ]  # 给所有方法加上装饰器, 可以加多个
#
#     def dispatch_request(self):
#         print('index')
#         return 'index'
#
#
# app.add_url_rule('/index', view_func=IndexView.as_view(name='index'))


# 第二种写法
class IndexView(views.MethodView):
    methods = ['GET']
    decorators = [timer, ]

    def get(self):
        time.sleep(2)
        return 'Index.GET'

    def post(self):
        return 'Index.POST'


app.add_url_rule('/index', view_func=IndexView.as_view(name='index'))

if __name__ == '__main__':
    app.run()
