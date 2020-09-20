from flask import Flask
import time
import functools

app = Flask(__name__)
app.debug = True


def timer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        reg = func(*args, **kwargs)
        print(time.time() - start_time)
        return reg
    return inner


@app.route('/index', methods=['GET', 'POST'])
@timer  # --->此时该考虑app装饰的是谁？是index还是我们定义的inner。答：inner
def index():
    time.sleep(3)
    return 'index'


@app.route('/order', methods=['GET', 'POST'])
@timer  #--->他的endpoint也等于inner此时就重名了,会出现AssertionError: View function mapping is overwriting an existing endpoint function: inner 解决通过functools解决
def order():
    return 'order'


if __name__ == '__main__':
    app.run()