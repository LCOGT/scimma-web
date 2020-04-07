from datetime import datetime
import json

from extensions import db


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    messages = db.relationship('Message', backref='topic', lazy=True)

    def __str__(self):
        return self.name

    @property
    def message_count(self):
        return Message.query.filter_by(topic_id=self.id).count()

    @property
    def latest_message(self):
        return db.session.query(Message).filter_by(topic_id=self.id).\
            order_by(Message.timestamp.desc()).first()

    def serialize(self):
        return {'name': self.name, 'messages': [message.serialize() for message in self.messages]}

    def save(self):
        db.session.add(self)
        db.session.commit()


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    content = db.Column(db.String(2048), nullable=False)
    timestamp = db.Column(db.DateTime, unique=False, nullable=False)
    ingestion_time = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.now)

    def serialize(self):
        serialized = {'id': self.id, 'timestamp': self.timestamp, 'topic': self.topic.name}
        serialized.update(json.loads(self.content))
        return serialized

    @property
    def url(self):
        number = json.loads(self.content).get('number')
        if self.topic.name.lower() == 'gcn':
            return f'https://gcn.gsfc.nasa.gov/gcn/gcn3/{number}.gcn3'
        elif self.topic.name.lower() == 'atel':
            return f'http://astronomerstelegram.org/?read={number}'
        return ''

    def save(self):
        db.session.add(self)
        db.session.commit()
