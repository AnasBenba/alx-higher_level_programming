#!/usr/bin/python3
"""script that takes your GitHub credentials
to display your id"""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    responde = requests.get(url, auth=HTTPBasicAuth(user, password))
    r = responde.json()
    print(r.get('id'))
