#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return 'Hello Word'


if __name__ == '__main__':
    app.run()