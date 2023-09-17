from apps.app import db
from datetime import datetime

class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.String, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)