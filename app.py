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


@app.route('/')
def index():
    # with stream.open('kafka://localhost:9092/gcn')
    return 'index'


@app.route('/publish', methods=['GET', 'POST'])
def publish():
    form = PublishForm(request.form)
    if request.method == 'POST' and form.validate():
        with Stream.open('kafka://{KAFKA_HOST}:{KAFKA_PORT}/{form.topic.data}', 'w', format='json') as s:
            s.write({'content': form.content.data})
    return render_template('publish_form.html', form=form)
    