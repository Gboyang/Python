from flask import Flask
from .views.account import ad
from .views.home import ac

app = Flask(__name__)

app.register_blueprint(ad)
app.register_blueprint(ac)
