#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, session

# template_folder 模板文件夹， 默认是templates
app = Flask(__name__, template_folder='template')
# secret_key 对我们下面session进行加密后返回给用户
app.secret_key = 'fdsfdsfsdfdsf'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('3.html')
    user = request.form.get('user')
    passwd = request.form.get('password')
    if user == 'yh' and passwd == '123123':
        session['user_info'] = user
        # 重定向
        return redirect('/index')
    else:
        return render_template('3.html', msg='用户密码错误')


@app.route('/index')
def index():
    # 判断session是否有用户信息
    if not session.get('user_info'):
        return redirect('/login')
    return '欢迎登陆'


@app.route('/logout')
def logout():
    # 删除session信息
    del session['user_info']
    return redirect('/login')


if __name__ == '__main__':
    app.run()
