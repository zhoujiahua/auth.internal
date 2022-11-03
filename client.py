#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
from requests.auth import HTTPBasicAuth

url = 'http://10.153.40.24:5000/api/user/token'
payload = {
    'email': 'jerry.zhou@advantest.com',
    'type': 'advantest',
    'username': 'jerry'
}
resp = requests.post(url, auth=HTTPBasicAuth('jerry', 'jerry.123'), data=payload)
print(resp.status_code, resp.json())
