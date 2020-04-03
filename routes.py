from flask import Blueprint, render_template, request

from scimma.client import stream

from client import ScimmaClientWrapper
from extensions import db
from forms import PublishForm
from models import Message, Topic


KAFKA_HOST = 'localhost'
# KAFKA_HOST = 'firkraag.lco.gtn'
KAFKA_PORT = '9092'

kafka_config = {
    'bootstrap.servers': f'{KAFKA_HOST}:{KAFKA_PORT}',
    'group.id': 'scimma-web-test',
    'auto.offset.reset': 'earliest'
}

client_wrapper = ScimmaClientWrapper(**kafka_config)

routes_bp = Blueprint('', 'routes')


@routes_bp.route('/', methods=['GET'])
def index():
    """
    Returns all messages
    """
    messages = Message.query.all()
    return {'messages': [message.serialize() for message in messages]}


@routes_bp.route('/topic/list', methods=['GET'])
def topic_list():
    """
    Returns the list of topics and number of messages per topic
    """
    return f'topics: {client_wrapper.topics()}'


@routes_bp.route('/topic/<id>', methods=['GET'])
def topic_get(id):
    """
    Returns the messages for a specific topic
    """
    messages = []

    # 'kafka://firkraag.lco.gtn:9092/test',
    with stream.open(f'kafka://{KAFKA_HOST}:{KAFKA_PORT}/{id}', 'r',
                     format='json', start_at='earliest') as s:
        for msg in s:
            if msg.error() in ['_PARTITION_EOF']:
                break;
            messages.append(msg)

    return f'{len(messages)} messages found for topic: {id}: {messages}'


@routes_bp.route('/message/create', methods=['GET', 'POST'])
def publish():
    """
    Allows a user to publish an alert to the given topic
    """
    form = PublishForm(request.form)
    form.topic.choices = [(topic, topic) for topic in client_wrapper.topics()]
    if request.method == 'POST' and form.validate():
        with stream.open(f'kafka://{KAFKA_HOST}:{KAFKA_PORT}/{form.topic.data}', 'w', format='json') as s:
            s.write({'content': form.content.data})
    return render_template('publish_form.html', form=form)


@routes_bp.route('/message/<int:msg_id>', methods=['GET'])
def message(msg_id):
    """
    Displays the content of a specific message
    """
    message = Message.query.get(msg_id)

    return message.serialize()
