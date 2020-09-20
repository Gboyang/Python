from flask import Flask, render_template, Markup


app = Flask(__name__)
app.debug = True


# 生成input框
@app.template_global()  #通过 @app.template_global()让每个模板中都能使用get_input
def get_input(value):
    # 前段通过safe后端Markup
    return Markup("<input value='%s'>" % value)


@app.route('/index', methods=['GET', 'POST'])
def index():
    dic = {
        'k1': 123,
        'k2': [11, 22, 33],
        'k3': {'name': '小明', 'age': 43},
        'k4': lambda x: x + 1,
        'k5': get_input
    }
    return render_template('index.html', **dic)


@app.route('/order', methods=['GET', 'POST'])
def order():
    return render_template('order.html')


if __name__ == '__main__':
    app.run()