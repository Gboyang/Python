from flask import Flask


app = Flask(__name__)
app.debug = True


# 随便定义一个函数通过@app.before_request
@app.before_request
def before_test1():
    print('前1')


@app.before_request
def before_test2():
    print('前2')


@app.after_request
def after_test1(response):   # @app.after_request 装饰后必须接受一个值，并返回。不然会出现错误
    print('后1')
    return response


@app.after_request
def after_test2(response):   # @app.after_request 装饰后必须接受一个值，并返回。不然会出现错误
    print('后2')
    return response


@app.route('/index', methods=['GET', 'POST'])
def index():
    print('执行了index')
    return 'INDEX'


if __name__ == '__main__':
    app.run()
