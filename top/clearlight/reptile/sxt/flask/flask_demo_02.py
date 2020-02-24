from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index')
def index():
    print(request)
    return render_template('index.html')


# post方式请求
@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request)
    uname = request.form['uname']
    password = request.form['password']
    return '正在登录' + '您的用户名是:' + uname + '密码是:' + password


# get方式请求
@app.route('/doget')
def do_get():
    print(request)
    uname = request.args['uname']
    return '正在测试do_get' + '用户名为:' + uname


if __name__ == '__main__':
    app.run(debug=1)
