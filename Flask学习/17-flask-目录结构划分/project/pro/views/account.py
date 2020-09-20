from flask import Blueprint, render_template, redirect,sessions


ad = Blueprint('ad', __name__)


@ad.before_request
def bf():
    print('before_request')


@ad.route('/login')
def login():
    return 'login'


@ad.route('/logout')
def logout():
    return 'logout'
