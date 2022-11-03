#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests

url = "http://10.153.40.24:5000/api/user/token"

payload = 'username=jerry&email=jerry.zhou%40advantest.com&type=advantest'
headers = {
    'Authorization': 'Basic YWRtaW46dGVzdDEyMw==',
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
