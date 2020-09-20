#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, session

# template_folder 模板文件夹， 默认是templates
app = Flask(__name__, template_folder='template')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('3.html')
    user = request.form.get('user')
    passwd = request.form.get('password')
    if user == 'yh' and passwd == '123123':
        # 我们都知道django中session是放入到数据库当中，但flask将session放哪了？
        # 答： 默认是放入到浏览器cookies中，如果就这样放人浏览器cookies中是不安全的。运行时也会出现如下错误
        # The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
        session['user_info'] = user
        # 重定向
        return redirect('/index')
    else:
        return render_template('3.html', msg='用户密码错误')


@app.route('/index')
def index():
    return '欢迎登陆'


if __name__ == '__main__':
    app.run()