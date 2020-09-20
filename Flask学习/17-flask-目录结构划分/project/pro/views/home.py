from flask import Blueprint

ac = Blueprint('ac', __name__)


@ac.route('/index')
def index():
    return 'index'
