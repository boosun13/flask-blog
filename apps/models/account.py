from apps.app import db
from datetime import datetime
from ulid import ULID
from pytz import timezone

class Account(db.Model):
    __tablename__ = 'accounts'
    __table_args__ = {'comment': 'アカウント情報'}

    id = db.Column(db.String(26), primary_key=True, default=str(ULID()))
    joined_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone('Asia/Tokyo')), comment='登録日時')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone('Asia/Tokyo')))
