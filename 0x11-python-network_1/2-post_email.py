#!/usr/bin/python3
"""Python script that takes in a URL and an email"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    param = f"'email': {sys.argv[2]}"
    data = urllib.parse.urlencode(param).encode('utf-8')
    request = urllib.request.Request(url, param=data, method='POST')
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
