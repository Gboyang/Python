#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, Request, render_template

app = Flask(__name__, template_folder='templates')
app.debug = True


@app.before_first_request
def before_first_request1():
    print('before_first_request1')


@app.before_first_request
def before_first_request2():
    print('before_first_request2')


@app.before_request
def before_request1():
    Request.nnn = 123
    print('before_request1')


@app.before_request
def before_request2():
    print('before_request2')


@app.after_request
def after_request1(response):
    print('before_request1', response)
    return response


@app.after_request
def after_request2(response):
    print('before_request2', response)
    return response


@app.errorhandler(404)   # 只有出现404执行
def page_not_found(error):
    return 'This page does not exist', 404


@app.template_global()
def sb(a1, a2):
    return a1 + a2


@app.template_filter()
def db(a1, a2, a3):
    return a1 + a2 + a3


@app.route('/')
def hello_world():
    return 'hello word'


if __name__ == '__main__':
    app.run()