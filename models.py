from datetime import datetime

from extensions import db

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    messages = db.relationship('Message', backref='topic', lazy=True)

    @property
    def num_messages(self):
        return -1


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    content = db.Column(db.String(256), nullable=False)
    timestamp = db.Column(db.DateTime, unique=False, nullable=False)
    ingestion_time = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.now)