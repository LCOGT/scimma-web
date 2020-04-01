from wtforms import Form, SelectField, StringField, validators


class PublishForm(Form):
    content = StringField('Message content', [validators.Length(max=500)])
    topic = SelectField('SCiMMA Topic', choices=[('gcn', 'GCN')])