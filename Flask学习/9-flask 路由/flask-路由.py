from flask import Flask

app = Flask(__name__)
app.debug = True

'''
点击查看route会发现他返回decorator
1、 执行decorator = app.route('/index', endpoint='index', methods=['GET', 'POST'])
2、 @decorator
        - decorator(index)
'''

# 方式一
@app.route('/index', endpoint='index', methods=['GET', 'POST'])
def index():
    print('请求来了')
    return 'hello word'


# 方式二、一般用上面的就行了
def order():
    return 'hello'


app.add_url_rule('/order', view_func=order)


if __name__ == '__main__':
    app.run()