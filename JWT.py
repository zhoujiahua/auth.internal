#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import jwt
import base64

payload = {'username': 'jerry', 'site': 'https://ops-coffee.cn'}
encoded_jwt = jwt.encode(payload, 'secret_key', algorithm='HS256')
decoded_jwt = jwt.decode(encoded_jwt, 'secret_key', algorithms=['HS256'])

print(decoded_jwt)
