from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

app = Flask(__name__)
app.config['TIMEZONE'] = 'Asia/Tokyo'

app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@db:5432/{os.getenv('DB_NAME')}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_ECHO=True,
)

# DB migration
db.init_app(app)
Migrate(app, db)

from apps.cli import seed_db_command

app.cli.add_command(seed_db_command)

from apps.models.account import Account
from apps.models.account_deletion import AccountDeletion
from apps.models.user import User

@app.route("/")
def current_account():
    account = Account.query.first()

    return f'<p>{account.id}</p>'

@app.route('/ping')
def ping():
    account = Account.query.first()

    return account.current_user.json()


@app.route('/account/<id>')
def account(id):
    account = Account.query.get(id)

    return f'This user\'s current email is \'{account.current_user.email}\''
