from datetime import datetime
import json

from extensions import db


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    messages = db.relationship('Message', backref='topic', lazy=True)

    @property
    def num_messages(self):
        return -1

    def serialize(self):
        return {'name': self.name, 'messages': [message.serialize() for message in self.messages]}

    def save(self):
        db.session.add(self)
        db.session.commit()


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    content = db.Column(db.String(256), nullable=False)
    timestamp = db.Column(db.DateTime, unique=False, nullable=False)
    ingestion_time = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.now)

    def serialize(self):
        serialized = {'id': self.id, 'timestamp': self.timestamp, 'topic': self.topic.name}
        serialized.update(json.loads(self.content))
        return serialized

    def save(self):
        db.session.add(self)
        db.session.commit()
