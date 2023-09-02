from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    a = 1 + 1

    return f'<p>{a}</p>'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
