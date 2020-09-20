#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__, template_folder='template')
app.secret_key = 'fdsfdsfsdfdsf'
app.debug = True  # 保存自动重启

# 为了更好展示这里定义一个字典模拟数据库中数据，默认应该从数据库拿数据
USER_DICT = {
    '1': {'name': '小米', 'age': 23},
    '2': {'name': '小明', 'age': 34},
    '3': {'name': '小强', 'age': 37},
    '4': {'name': '多哥', 'age': 25}
}


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


@app.route('/index', endpoint='index') # endpoint='index' 别名
def index():
    # 判断session是否有用户信息
    if not session.get('user_info'):
        return redirect('/login')
    return render_template('4.html', user_dict=USER_DICT)


@app.route('/detail')
def detail():
    if not session.get('user_info'):
        return redirect('/login')
    uid = request.args.get('uid')
    info = USER_DICT.get(uid)
    return render_template('detail.html', info=info)

@app.route('/logout')
def logout():
    # 删除session信息
    del session['user_info']
    return redirect('/login')


if __name__ == '__main__':
    app.run()
