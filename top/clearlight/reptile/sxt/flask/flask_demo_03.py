from flask import Flask, render_template, request, url_for, redirect, abort, make_response

app = Flask(__name__)


@app.route('/str')
def return_str():
    return '返回了str'


@app.route('/page')
def return_page():
    # return '返回了一个页面'
    return render_template('index.html', msg='登录用户名或密码错误')


# post方式请求
@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request)
    uname = request.form['uname']
    password = request.form['password']
    return '正在登录' + '您的用户名是:' + uname + '密码是:' + password


@app.route('/index')
def return_url():
    # return '返回了一个url'
    return redirect(url_for('return_page'))


@app.route('/code')
def return_error():
    # return '返回一个状态码'
    abort(405)


@app.route("/set")
def return_set():
    # return '返回了一个自定义响应'
    response = make_response("返回一个自定义的响应")
    response.headers["cookie"] = 'abc'
    return response


if __name__ == '__main__':
    app.run(debug=1)
