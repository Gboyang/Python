from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def index1():
    return 'Index1'


class MiddleWare:
    def __init__(self, wsgi_app):
        '''
            服务端启动时执行
        '''
        self.wsgi_app = wsgi_app

    def __call__(self, *args, **kwargs):
        '''
            每次用户请求到来时会执行
        '''
        print('before')
        obj = self.wsgi_app(*args, **kwargs)
        print('after')
        return obj


if __name__ == "__main__":
    app.wsgi_app = MiddleWare(app.wsgi_app)
    app.run()
