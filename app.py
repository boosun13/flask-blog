from flask import Flask
from database import init_db

app = Flask(__name__)
app.config.from_object('config.Config')

# DB init
init_db(app)

@app.route("/")
def hello_world():
    a = 1 + 1

    return f'<p>{a}</p>'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
