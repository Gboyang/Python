from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

'''
@app.route('/user/<username>')
@app.route('/post/<int:post_id>')
@app.route('/post/<float:post_id>')
@app.route('/post/<path:path>')
@app.route('/login', methods=['GET', 'POST'])

常用路由系统有以上五种，所有的路由系统都是基于一下对应关系来处理：
DEFAULT_CONVERTERS = {
    'default':          UnicodeConverter,
    'string':           UnicodeConverter,
    'any':              AnyConverter,
    'path':             PathConverter,
    'int':              IntegerConverter,
    'float':            FloatConverter,
    'uuid':             UUIDConverter,
}
'''


@app.route('/index/<int:nid>', methods=['GET', 'POST'])
def index(nid):
    print(nid)
    return 'Index'


if __name__ == '__main__':
    app.run()