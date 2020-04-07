from flask import abort, Blueprint, redirect, render_template, request, url_for

from scimma.client import stream

from client import ScimmaClientWrapper
# from extensions import db
from forms import CreateTopicForm, PublishForm
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

api_bp = Blueprint('', 'api')


@api_bp.route('/message',  methods=['GET'])
def message_list():
    pass


@api_bp.route('/message/create', methods=['POST'])
def message_create():
    pass


@api_bp.route('/message/get', methods=['GET'])
def message_get():
    pass


@api_bp.route('/message/update', methods=['POST'])
def message_update():
    pass


@api_bp.route('/message/delete', methods=['DELETE'])
def message_delete():
    pass


@api_bp.route('/topic',  methods=['GET'])
def topic_list():
    pass


@api_bp.route('/topic/create', methods=['POST'])
def topic_create():
    pass


@api_bp.route('/topic/get', methods=['GET'])
def topic_get():
    pass


@api_bp.route('/topic/update', methods=['POST'])
def topic_update():
    pass


@api_bp.route('/topic/delete', methods=['DELETE'])
def topic_delete():
    pass
