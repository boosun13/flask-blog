from apps.app import db
from datetime import datetime
from ulid import ULID
from pytz import timezone

class AccountDeletion(db.Model):
    __tablename__ = 'account_deletions'
    __table_args__ = {'comment': 'アカウントの削除情報'}

    id = db.Column(db.String(26), primary_key=True, default=str(ULID()))
    account_id = db.Column(db.String(26), db.ForeignKey('accounts.id'), nullable=False, unique=True, index=True)
    registered_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone('Asia/Tokyo')), comment='退会日時')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone('Asia/Tokyo')))

    # relationships
    account = db.relationship('Account', backref='account_deletion', lazy=True, uselist=False)