from app import app
from client import ScimmaClientWrapper
from extensions import db
from models import Message, Topic


def ingest_alert(msg):
    with app.app_context():
        topic = db.session.query(Topic).filter_by(name=msg.topic())[0]
        if not topic:
            topic = db.session.add(Topic(name=msg.topic()))
            db.session.commit()

        message = Message(
            content=msg.value(),
            timestamp=msg.timestamp(),
        )

        topic.messages.append(message)

        db.session.add(message)
        db.session.commit()


def run_ingest():
    client = ScimmaClientWrapper(**{'bootstrap.servers': 'localhost:9092', 'group.id': 'scimma-web-test'})

    client.consumer.subscribe(client.topics())

    while True:
        msg = client.consumer.poll(1)
        if msg is None:
            continue
        if msg.error():
            print(msg.error())
            continue

        ingest_alert(msg)

    client.consumer.close()


if __name__ == '__main__':
    run_ingest()