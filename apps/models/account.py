from apps.app import db
from datetime import datetime
from ulid import ULID


class Account(db.Model):
    __tablename__ = 'accounts'
    __table_args__ = {'comment': 'アカウント情報'}

    id = db.Column(db.String(26), primary_key=True, default=str(ULID()))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
