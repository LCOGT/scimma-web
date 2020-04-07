from datetime import datetime
import json

from app import app
from client import ScimmaClientWrapper
from extensions import db
from models import Message, Topic


def ingest_alert(msg):
    print('ingesting alert')
    with app.app_context():
        topic = db.session.query(Topic).filter_by(name=msg.topic()).first()
        if not topic:
            topic = Topic(name=msg.topic())
            db.session.add(topic)
            db.session.commit()

        message = Message(
            content=msg.value().decode('utf-8'),
            timestamp=datetime.fromtimestamp(msg.timestamp()[1]/1000.0),
        )

        topic.messages.append(message)

        db.session.add(message)
        db.session.commit()


def run_ingest():
    client = ScimmaClientWrapper(**{
        'bootstrap.servers': 'localhost:9092', 'group.id': 'scimma-web-test', 'auto.offset.reset': 'earliest'
    })

    client.consumer.subscribe(client.topics())

    while True:
        print('polling')
        msg = client.consumer.poll(5)
        if msg is None:
            continue
        if msg.error():
            print(msg.error())
            continue

        ingest_alert(msg)

    client.consumer.close()


if __name__ == '__main__':
    run_ingest()
