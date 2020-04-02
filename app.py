from datetime import datetime

from flask import Flask, render_template, request

from scimma.client import stream

from client import ScimmaClientWrapper
from forms import PublishForm

# KAFKA_HOST = 'localhost'
KAFKA_HOST = 'firkraag.lco.gtn'
KAFKA_PORT = '9092'


kafka_config = {
    'bootstrap.servers': f'{KAFKA_HOST}:{KAFKA_PORT}',
    'group.id': 'scimma-web-test'
}

app = Flask(__name__)
client_wrapper = ScimmaClientWrapper(**kafka_config)


@app.route('/', methods=['GET'])
def index():
    """
    Returns the list of topics and number of messages per topic
    """
    topics = client_wrapper.topics()
    return f'topics: {topics}'


@app.route('/publish', methods=['GET', 'POST'])
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


@app.route('/topic/<id>', methods=['GET'])
def topic(id):
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


@app.route('/topic/<t_id>/message/<msg>', methods=['GET'])
def message(t_id, msg):
    """
    Displays the content of a specific message
    """
    return f'message ({msg}) from topic {t_id} <not-implemented>'
