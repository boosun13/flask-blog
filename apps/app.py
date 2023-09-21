from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@db:5432/{os.getenv('DB_NAME')}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_ECHO=True,
)

# DB migration
db.init_app(app)
Migrate(app, db)

from apps.models.account import Account
# from apps.models.user import User
from apps.models.account_deletion import AccountDeletion

@app.route("/")
def hello_world():
    a = Account.query.count()

    if a == 0:
        # Create a new account
        account = Account()
        db.session.add(account)
        db.session.commit()
        a = Account.query.count()

    return f'<p>{a}</p>'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
