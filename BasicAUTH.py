#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask, jsonify, request
import base64

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Hi Flask'


@app.route('/api/user/token', methods=['POST'])
def user_token():
    user = request.values.to_dict()
    auth = request.headers.get('Authorization', None)
    auth_key = auth.split(' ')[1] if auth else None
    decode_key = base64.b64decode(auth_key).decode('utf-8') if auth_key else None
    print(auth_key, decode_key)
    return jsonify(user), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
