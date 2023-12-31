from apps.app import db
from datetime import datetime
from ulid import ULID
from pytz import timezone
from werkzeug.security import generate_password_hash


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'comment': 'アカウントのユーザー情報'}

    id = db.Column(db.String(26), primary_key=True, default=str(ULID()))
    account_id = db.Column(db.String(26),db.ForeignKey('accounts.id'), nullable=False, index=True)
    email = db.Column(db.String(255), nullable=False, comment='登録メールアドレス')
    password_hash = db.Column(db.String, comment='ハッシュ化されたパスワード')
    registered_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone('Asia/Tokyo')), comment='登録日時')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone('Asia/Tokyo')))

    # relationships
    account = db.relationship('Account', back_populates='users', lazy=True, uselist=False)

    # NOTE: property for password
    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

