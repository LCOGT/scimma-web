from confluent_kafka import Consumer, Producer
from confluent_kafka.admin import AdminClient


class ScimmaClientWrapper:
    def __init__(self, *args, **kwargs):
        self.consumer = Consumer(kwargs)
        self.producer = Producer(kwargs)
        self.admin_client = AdminClient(kwargs)

    def topics(self):
        # Topic set always contains partition offset information topic called __consumer_offsets
        return [topic for topic in self.admin_client.list_topics().topics if '__consumer_offsets' not in topic]

    def current_messages(self, topic):
        msg = self.consumer.consume(num_messages=1)
        while True:
            msg = self.consumer.poll(1)
            if msg:
                print(msg.error())
                break

    def get_messages(self, topics=None):
        if not topics:
            topics = self.topics()
        self.consumer.subscribe(topics)
        while True:
            print('polling')
            msg = self.consumer.poll(1)
            print(msg)
            if msg:
                print(msg.value())
                print(msg.error())
                break