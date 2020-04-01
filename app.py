from flask import Flask, render_template, request

from scimma.client.io import Stream

from wtforms import Form, SelectField, StringField, validators


class PublishForm(Form):
    content = StringField('Message content', [validators.Length(max=500)])
    topic = SelectField('SCiMMA Topic', choices=[('gcn', 'GCN')])


# KAFKA_HOST = 'localhost'
KAFKA_HOST = 'firkraag.lco.gtn'
KAFKA_PORT = '9092'


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    Returns the list of topics and number of messages per topic
    """
    # with stream.open('kafka://localhost:9092/gcn')
    return 'index'


@app.route('/publish', methods=['GET', 'POST'])
def publish():
    """
    Allows a user to publish an alert to the given topic
    """
    form = PublishForm(request.form)
    if request.method == 'POST' and form.validate():
        with Stream.open('kafka://{KAFKA_HOST}:{KAFKA_PORT}/{form.topic.data}', 'w', format='json') as s:
            s.write({'content': form.content.data})
    return render_template('publish_form.html', form=form)


@app.route('/topic/<str>', methods=['GET'])
def topic(pk):
    """
    Returns the messages for a specific topic
    """
    return 'topic'


@app.route('/topic/<str>/message/<id>', methods=['GET'])
def message(pk):
    """
    Displays the content of a specific message
    """
    return 'message'