#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

# template_folder 模板文件夹， 默认是templates
app = Flask(__name__, template_folder='template')


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('2.html')
    # request.args 获取GET传来的值
    # request.form 获取POST传过来的值
    v1 = request.form.get('v1')
    v2 = request.form.get('v2')
    v3 = int(v1) + int(v2)
    # render_template('2.html', v3=v3) # 等同于下面的
    return render_template('2.html', **{'v3': v3})


if __name__ == '__main__':
    app.run()