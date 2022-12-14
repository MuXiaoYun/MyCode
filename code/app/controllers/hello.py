# -*- coding: utf-8 -*-
from flasgger import swag_from
from flask import Blueprint, g, jsonify, render_template, send_from_directory

from .login_required import login_required

bp = Blueprint(
    'hello',
    __name__,
    template_folder='../templates'
)


@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@bp.route('/<path:path>')
def handle(path):
    return render_template('index.html')


@bp.route('/stickers/<path:path>', methods=['GET'])
def send(path):
    print(path)
    return send_from_directory('stickers', path)


@bp.route('/api/v1/hello', methods=['GET'])
@swag_from('swagger/hello.yml')
def hello_world():
    return jsonify({'message': "Hello world"}), 200


@bp.route('/api/v1/hello-user', methods=['GET'])
@login_required
def hello_user():
    return jsonify({'message': "Hello world, " + g.user_name}), 200
