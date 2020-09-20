from flask import Flask

app = Flask(__name__)
# 通过下面的指定settings文件路径， 手动创建settings文件。所有配置都写到settings文件中
app.config.from_object('settings.Config')


@app.route('/index', endpoint='index', methods=['GET', 'POST'])
def index():
    print('请求来了')
    return 'hello word'


if __name__ == '__main__':
    app.run()