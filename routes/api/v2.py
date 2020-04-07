from flask import abort, Blueprint, redirect, render_template, request, url_for

from forms import CreateTopicForm, PublishForm
from models import Message, Topic

api_bp = Blueprint('/v2', 'api_v2')


@api_bp.route('/v2/message',  methods=['GET'])
def message_list():
    return 'v2'
