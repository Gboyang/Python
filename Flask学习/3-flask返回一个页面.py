#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template

# template_folder 模板文件夹， 默认是templates
app = Flask(__name__, template_folder='template')


@app.route('/index')
def index():
    return render_template('1.html')


if __name__ == '__main__':
    app.run()