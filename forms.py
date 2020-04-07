from wtforms import Form, IntegerField, SelectField, StringField, SubmitField, validators


class PublishForm(Form):
    title = StringField('Message title', [validators.Length(max=80)])
    number = IntegerField('Message number')
    subject = StringField('Message subject', [validators.Length(max=80)])
    publisher = StringField('Publisher name', [validators.Length(max=80)])
    content = StringField('Message content', [validators.Length(max=1024)])
    topic = SelectField('SCiMMA Topic', choices=[('gcn', 'GCN')])
    submit = SubmitField()


class CreateTopicForm(Form):
    topic_name = StringField('Topic name', [validators.Length(max=80)])
    submit = SubmitField()
