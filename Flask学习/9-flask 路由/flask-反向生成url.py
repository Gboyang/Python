from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.debug = True


@app.route('/he1', endpoint='he1', methods=['GET', 'POST'])
def he1():
    # flask 中通过url_for 来查找别名对应的url
    h1 = url_for('he1')
    h2 = url_for('he2')
    h3 = url_for('he3')
    print(h1, h2, h3)
    return 'hello he1'


@app.route('/he2', endpoint='he2', methods=['GET', 'POST'])
def index():
    print('请求来了')
    return 'hello he2'


@app.route('/he3', endpoint='he3', methods=['GET', 'POST'])
def index():
    print('请求来了')
    return 'hello he3'


if __name__ == '__main__':
    app.run()