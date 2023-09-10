from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=f"postgresql://{os.getenv('DB_USER')}:{os.getenv(
        'DB_PASSWORD')}@db:5432/{os.getenv('DB_NAME')}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# DB migration
db.init_app(app)
Migrate(app, db)


@app.route("/")
def hello_world():
    a = 1 + 1

    return f'<p>{a}</p>'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
