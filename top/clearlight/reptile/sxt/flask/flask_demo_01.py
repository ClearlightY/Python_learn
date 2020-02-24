from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Flask'


@app.route('/index')
def index():
    return 'index'


@app.route('/hello/<name>')
def test_path(name):
    return name+'?'


if __name__ == '__main__':
    app.run(debug=1)