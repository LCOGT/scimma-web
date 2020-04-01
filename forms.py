from wtforms import Form, SelectField, StringField, SubmitField, validators


class PublishForm(Form):
    content = StringField('Message content', [validators.Length(max=500)])
    topic = SelectField('SCiMMA Topic', choices=[('gcn', 'GCN')])
    submit = SubmitField()