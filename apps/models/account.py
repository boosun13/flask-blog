from apps.app import db
from datetime import datetime
from ulid import ULID

class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.String(26), primary_key=True, default=str(ULID()))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)