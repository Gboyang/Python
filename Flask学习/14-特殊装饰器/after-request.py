from flask import Flask


app = Flask(__name__)
app.debug = True


# 随便定义一个函数通过@app.before_request
@app.before_request
def test1():
    print('执行前')


@app.after_request
def test2(response):   # @app.after_request 装饰后必须接受一个值，并返回。不然会出现错误
    print('执行后')
    return response


@app.route('/index', methods=['GET', 'POST'])
def index():
    print('执行了index')
    return 'INDEX'


@app.route('/home', methods=['GET', 'POST'])
def home():
    print('执行了home')
    return 'HOME'


if __name__ == '__main__':
    app.run()
