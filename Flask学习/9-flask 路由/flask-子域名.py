from flask import Flask, views, url_for

app = Flask(__name__)
app.debug = True
app.config["SERVER_NAME"] = 'cnccboy.com:5000'


@app.route('/dynamic', subdomain='<username>')
def index(username):
    print(username)
    return 'dsadsadad'


if __name__ == '__main__':
    app.run()
