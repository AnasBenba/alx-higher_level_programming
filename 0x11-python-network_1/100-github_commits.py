#!/usr/bin/python3
"""script that takes your GitHub credentials
to display your id"""
import requests
import sys


if __name__ == "__main__":
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    responde = requests.get(url)
    r = responde.json()
    count = 0
    for i in r[:10]:
        print(f"{i.get('sha')}: {i.get('commit').get('author').get('name')}")
