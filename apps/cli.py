import click
from flask.cli import with_appcontext
from apps.app import db
from apps.models.account import Account
from apps.models.user import User

@click.command('seed-db')
@with_appcontext
def seed_db_command():
    """Seed the database with initial data."""
    seed_db()
    click.echo('Seeded the database.')

def seed_db():
    """Seed the database with initial data."""
    account = Account()
    user = User(email='test@example.com', account=account)

    db.session.add(account)
    db.session.add(user)
    db.session.commit()