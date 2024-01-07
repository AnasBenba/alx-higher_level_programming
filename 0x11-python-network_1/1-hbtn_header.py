#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    content = response.read()
    headers = response.info()
    if "X-Request-Id" in headers:
        print(headers['X-Request-Id'])
