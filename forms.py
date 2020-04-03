from wtforms import Form, SelectField, StringField, SubmitField, validators


class PublishForm(Form):
    content = StringField('Message content', [validators.Length(max=256)])
    topic = SelectField('SCiMMA Topic', choices=[('gcn', 'GCN')])
    submit = SubmitField()


class CreateTopicForm(Form):
    topic_name = StringField('Topic name', [validators.Length(max=80)])
    submit = SubmitField()
    