from confluent_kafka import Consumer, Producer
from confluent_kafka.admin import AdminClient


class ScimmaClientWrapper:
    def __init__(self, *args, **kwargs):
        self.consumer = Consumer(kwargs)
        self.producer = Producer(kwargs)
        self.admin_client = AdminClient(kwargs)

    def topics(self):
        metadata = [topic_metadata for topic_name, topic_metadata in self.admin_client.list_topics().topics.items()]
        for md in metadata:
            print(metadata)
        return self.admin_client.list_topics().topics.items()

    def current_messages(self, topic):
        msg = self.consumer.consume(num_messages=1)
        while True:
            msg = self.consumer.poll(1)
            if msg:
                print(msg.error())
                break