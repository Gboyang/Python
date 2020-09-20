from flask import Flask, flash, sessions, get_flashed_messages


# 本质就是通过sessions来做的
app = Flask(__name__)
app.debug = True
app.secret_key = 'dasdasd'


@app.route('/x1', methods=['GET', 'POST'])
def x1():
    flash('hello word 1', category='x1')  # category 表示分类
    flash('hello word 2', category='x2')
    return '视图函数1'


@app.route('/x2', methods=['GET', 'POST'])
def x2():
    # data = get_flashed_messages()  # 拿取所有
    data = get_flashed_messages(category_filter=['x1'])  # 可以添加多个
    print(data)
    return '视图函数2'


if __name__ == '__main__':
    app.run()